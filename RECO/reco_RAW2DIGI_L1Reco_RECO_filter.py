# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: reco -s RAW2DIGI,L1Reco,RECO --filein file:/mnt/hadoop/cms/store/user/tawei/Data_samples/HIRun2011/HIDiMuon/RAW/v1/000/183/013/02A69E73-C01F-E111-A008-00237DDC5AF6.root --fileout reco_test.root --scenario HeavyIons --conditions GR_R_53_LV6::All --eventcontent RECODEBUG --datatier RECO --repacked --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(-1)
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
#    fileNames = cms.untracked.vstring('file:/mnt/hadoop/cms/store/user/tawei/Data_samples/HIRun2011/HIDiMuon/RAW/v1/000/183/013/02A69E73-C01F-E111-A008-00237DDC5AF6.root')
    fileNames = cms.untracked.vstring('file:/mnt/hadoop/cms/store/user/tawei/Data_samples/HIRun2011/HIDiMuon/USER/L2DoubleMu3Skim_v10_38dff9fa051006d6e895e3c1df676d76-v1/40000/02F09DEB-FACF-E411-9976-7845C4FB82F2.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('reco nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

#A jpsi filter
process.JpsiFilter = cms.EDFilter("JpsiFilter",
    doJpsiFilter = cms.untracked.bool(True),
	MuonLabel = cms.untracked.InputTag('muons')
)
process.pJpsiFilter = cms.Path(process.JpsiFilter)

process.RECODEBUGoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECODEBUGEventContent.outputCommands,
    fileName = cms.untracked.string('reco.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('pJpsiFilter') ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RECO')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_53_LV6::All', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstructionHeavyIons)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECODEBUGoutput_step = cms.EndPath(process.RECODEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.pJpsiFilter,process.endjob_step,process.RECODEBUGoutput_step)

from Configuration.PyReleaseValidation.ConfigBuilder import MassReplaceInputTag
MassReplaceInputTag(process)

