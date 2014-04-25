import sys
from services.spawn import MobileTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	templates = Vector()
	templates.add('object/mobile/shared_womp_rat.iff')
	mobileTemplate.setCreatureName('womprat')
	mobileTemplate.setTemplates(templates)
	mobileTemplate.setAttackRange(5)
	mobileTemplate.setAttackSpeed(5)
	mobileTemplate.setLevel(5)
	mobileTemplate.setAttackRange(3)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(6)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	core.spawnService.addMobileTemplate('womprat', mobileTemplate)
	