# File: C (Python 2.4)

from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE17a',
        'wantDoors': 1 },
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None },
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [] },
    10020: {
        'type': 'attribModifier',
        'name': 'range',
        'comment': '',
        'parentEntId': 10016,
        'attribName': 'range',
        'recursive': 1,
        'typeName': 'stomper',
        'value': '7.3' },
    10026: {
        'type': 'attribModifier',
        'name': 'period',
        'comment': '',
        'parentEntId': 10016,
        'attribName': 'period',
        'recursive': 1,
        'typeName': 'stomper',
        'value': '6' },
    10011: {
        'type': 'conveyorBelt',
        'name': 'conveyorBelt',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(3.37029790878, 24.420026779200001, 13.000869751),
        'hpr': Point3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'platformcollision',
        'length': 42.0,
        'speed': 2.0,
        'treadLength': 10.0,
        'treadModelPath': 'phase_9/models/cogHQ/platform1',
        'widthScale': 1.0 },
    10014: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10013,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.2,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 8,
        'velocity': 4 },
    10025: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10022,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.2,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 8,
        'velocity': 4 },
    10002: {
        'type': 'healBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-1.80931818485, 65.054122924799998, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0 },
    10008: {
        'type': 'mintShelf',
        'name': 'frontShelf',
        'comment': '',
        'parentEntId': 10007,
        'pos': Point3(0.75479054451000005, -116.741004944, 0.0),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10009: {
        'type': 'mintShelf',
        'name': 'backShelf1',
        'comment': '',
        'parentEntId': 10007,
        'pos': Point3(5.0981316566499997, 63.660175323499999, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10010: {
        'type': 'mintShelf',
        'name': 'copy of backShelf1',
        'comment': '',
        'parentEntId': 10007,
        'pos': Point3(-3.8019716739699998, 81.760208129899993, 0.0),
        'hpr': Vec3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10000: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0.0, -9.59561252594, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10003: {
        'type': 'model',
        'name': 'downLift',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(4.4395956993099999, 36.985065460199998, 0.88027894496900005),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(0.55000001192100001, 0.55000001192100001, 0.55000001192100001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer.bam' },
    10004: {
        'type': 'model',
        'name': 'upLift',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-3.2559578418699999, -35.5523605347, 0.88027894496900005),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(0.55000001192100001, 0.55000001192100001, 0.55000001192100001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer.bam' },
    10012: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0.0, 10.1246709824, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10023: {
        'type': 'model',
        'name': 'penaltyLift',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-4.4634590148899997, -13.5, 0.88027894496900005),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(0.34999999403999998, 0.34999999403999998, 0.34999999403999998),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer.bam' },
    10027: {
        'type': 'model',
        'name': 'shadow',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0.0, 0.0, -1.5657727718400001),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(3.5935189724000001, 3.5935189724000001, 3.5935189724000001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cogHQ/RoundShadow.bam' },
    10028: {
        'type': 'model',
        'name': 'shadow',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, -1.5657727718400001),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(3.5935189724000001, 3.5935189724000001, 3.5935189724000001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cogHQ/RoundShadow.bam' },
    10029: {
        'type': 'model',
        'name': 'copy of shadow',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(0.0, 0.0, -2.4700000286099999),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(3.5935189724000001, 3.5935189724000001, 3.5935189724000001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cogHQ/RoundShadow.bam' },
    10001: {
        'type': 'nodepath',
        'name': 'crates',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.66049700975400005, 0.0, 0.013348489068400001),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.5057501792900001, 2.5057501792900001, 2.5057501792900001) },
    10007: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10016: {
        'type': 'nodepath',
        'name': 'stompers',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(5.0, 10.438042640700001, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10021: {
        'type': 'nodepath',
        'name': 'goons',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10005: {
        'type': 'paintMixer',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0.0, 0.0, 3.5645427703900001),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'PaintMixerFloorCollision',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer',
        'modelScale': Vec3(1.0, 1.0, 1.0),
        'motion': 'noBlend',
        'offset': Point3(0.0, 0.0, 20.0),
        'period': 10.0,
        'phaseShift': 0.0,
        'shaftScale': 2.5,
        'waitPercent': 0.40000000000000002 },
    10006: {
        'type': 'paintMixer',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 3.5645427703900001),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'PaintMixerFloorCollision',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer',
        'modelScale': Vec3(1.0, 1.0, 1.0),
        'motion': 'noBlend',
        'offset': Point3(0.0, 0.0, 20.0),
        'period': 5.0,
        'phaseShift': 0.0,
        'shaftScale': 2.5,
        'waitPercent': 0.40000000000000002 },
    10024: {
        'type': 'paintMixer',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(0.0, 0.0, 3.5645427703900001),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'PaintMixerFloorCollision',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer',
        'modelScale': Vec3(1.0, 1.0, 1.0),
        'motion': 'noBlend',
        'offset': Point3(0.0, 0.0, 33.0),
        'period': 10.0,
        'phaseShift': 0.5,
        'shaftScale': 4.0,
        'waitPercent': 0.40000000000000002 },
    10013: {
        'type': 'path',
        'name': 'right',
        'comment': '',
        'parentEntId': 10021,
        'pos': Point3(4.0, 0.0, 0.0),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 3,
        'pathScale': 1.0 },
    10022: {
        'type': 'path',
        'name': 'left',
        'comment': '',
        'parentEntId': 10021,
        'pos': Point3(-4.0, 2.0, 0.0),
        'hpr': Point3(-90.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 3,
        'pathScale': 1.0 },
    10015: {
        'type': 'stomper',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10016,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(4.0, 2.0, 4.0),
        'modelPath': 0,
        'motion': 1,
        'period': 6,
        'phaseShift': 0.0,
        'range': 7.2999999999999998,
        'shaftScale': Point3(1.8999999761599999, 7.5, 1.8999999761599999),
        'soundLen': 0,
        'soundOn': 0,
        'soundPath': 0,
        'style': 'horizontal',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 0,
        'zOffset': 0 },
    10017: {
        'type': 'stomper',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10016,
        'pos': Point3(0.0, 8.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(4.0, 2.0, 4.0),
        'modelPath': 0,
        'motion': 1,
        'period': 6,
        'phaseShift': 0.75,
        'range': 7.2999999999999998,
        'shaftScale': Point3(1.8999999761599999, 7.5, 1.8999999761599999),
        'soundLen': 0,
        'soundOn': 0,
        'soundPath': 0,
        'style': 'horizontal',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 0,
        'zOffset': 0 },
    10018: {
        'type': 'stomper',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10016,
        'pos': Point3(0.0, 16.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(4.0, 2.0, 4.0),
        'modelPath': 0,
        'motion': 1,
        'period': 6,
        'phaseShift': 0.25,
        'range': 7.2999999999999998,
        'shaftScale': Point3(1.8999999761599999, 7.5, 1.8999999761599999),
        'soundLen': 0,
        'soundOn': 0,
        'soundPath': 0,
        'style': 'horizontal',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 0,
        'zOffset': 0 },
    10019: {
        'type': 'stomper',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10016,
        'pos': Point3(0.0, 24.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(4.0, 2.0, 4.0),
        'modelPath': 0,
        'motion': 1,
        'period': 6,
        'phaseShift': 0.5,
        'range': 7.2999999999999998,
        'shaftScale': Point3(1.8999999761599999, 7.5, 1.8999999761599999),
        'soundLen': 0,
        'soundOn': 0,
        'soundPath': 0,
        'style': 'horizontal',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 0,
        'zOffset': 0 } }
Scenario0 = { }
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0] }
