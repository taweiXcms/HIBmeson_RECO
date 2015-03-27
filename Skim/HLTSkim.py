#Simple HLT skim .py.
#Ta-Wei Wang: twang@cern.ch
import FWCore.ParameterSet.Config as cms

process = cms.Process('SKElectron')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.Skims_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(
        'file:/mnt/hadoop/cms/store/user/tawei/Data_samples/HIRun2011/HIDiMuon/RAW/v1/000/183/013/02A69E73-C01F-E111-A008-00237DDC5AF6.root'
    )
)

import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHI = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
#process.hltHI.HLTPaths = ["HLT_HIL2DoubleMu3_v1", "HLT_HIL2DoubleMu3_v2"]
process.hltHI.HLTPaths = ["HLT_HIL2DoubleMu3_v*"]
process.hltHI.throw = False
process.hltHI.andOr = True
process.hltfilter = cms.Path (process.hltHI)

# Output definition
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('test.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('hltfilter') ),
)

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:com10', '')

# Schedule definition
process.p = cms.EndPath(process.out)
process.schedule = cms.Schedule(process.hltfilter, process.p)
