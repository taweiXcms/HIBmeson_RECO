// -*- C++ -*-
//
// Package:    JpsiFilter
// Class:      JpsiFilter
// 
/**\class JpsiFilter JpsiFilter.cc HIBmeson_RECO/JpsiFilter/src/JpsiFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Ta-Wei Wang
//         Created:  Mon Mar 23 16:44:58 EDT 2015
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//Muon
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "TLorentzVector.h"
#define MUON_MASS   0.10565837
#define PION_MASS   0.13957018
#define KAON_MASS   0.493677
#define KSHORT_MASS 0.497614
#define KSTAR_MASS  0.89594
#define PHI_MASS    1.019455
#define JPSI_MASS   3.096916
#define PSI2S_MASS  3.686109

//
// class declaration
//

class JpsiFilter : public edm::EDFilter {
   public:
      explicit JpsiFilter(const edm::ParameterSet&);
      ~JpsiFilter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual bool beginRun(edm::Run&, edm::EventSetup const&);
      virtual bool endRun(edm::Run&, edm::EventSetup const&);
      virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------
     bool doJpsiFilter_;
     edm::InputTag muonLabel_;
     
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
JpsiFilter::JpsiFilter(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
   doJpsiFilter_ = iConfig.getUntrackedParameter<bool>("doJpsiFilter",true);
   muonLabel_ = iConfig.getUntrackedParameter<edm::InputTag>("MuonLabel",edm::InputTag("muons"));
}


JpsiFilter::~JpsiFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
JpsiFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;
#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif

#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif

	//jpsi filter
    if(doJpsiFilter_){
		TLorentzVector v1,v2,vsum;
        Handle<reco::MuonCollection> muons;
        iEvent.getByLabel(muonLabel_, muons);
        for( reco::MuonCollection::const_iterator it1 = muons->begin();
            it1 != muons->end(); it1++ ) {
			if(it1->charge()<0) continue;
            if(!muon::isGoodMuon(*it1,muon::TMOneStationTight)) continue;
            if(fabs(it1->eta()) < 1.3) {if(it1->pt() < 3.3) continue;}
            else if(fabs(it1->eta()) > 1.3 && fabs(it1->eta()) < 2.2) {if(it1->p() < 2.9) continue;}
            else if(fabs(it1->eta()) > 2.2 && fabs(it1->eta()) < 2.4) {if(it1->pt() < 0.8) continue;}
            else {continue;}
            for( reco::MuonCollection::const_iterator it2 = muons->begin();
                it2 != muons->end(); it2++ ) {
                if (it2->charge()>0) continue;
                if(!muon::isGoodMuon(*it2,muon::TMOneStationTight)) continue;
                if(fabs(it2->eta()) < 1.3) {if(it2->pt() < 3.3) continue;}
                else if(fabs(it2->eta()) > 1.3 && fabs(it2->eta()) < 2.2) {if(it2->p() < 2.9) continue;}
                else if(fabs(it2->eta()) > 2.2 && fabs(it2->eta()) < 2.4) {if(it2->pt() < 0.8) continue;}
                else {continue;}
                v1.SetXYZM(it1->px(),it1->py(),it1->pz(),MUON_MASS);
                v2.SetXYZM(it2->px(),it2->py(),it2->pz(),MUON_MASS);
                vsum = v1 + v2;
				if(fabs(vsum.Mag()-JPSI_MASS)<0.4) 
                if(vsum.Pt()>3)
					return true;
            }
        }
    }
    //return true;
    return false;
}

// ------------ method called once each job just before starting event loop  ------------
void 
JpsiFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JpsiFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
JpsiFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
JpsiFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
JpsiFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
JpsiFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JpsiFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(JpsiFilter);
