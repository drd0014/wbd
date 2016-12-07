import Navigation.prod.Fix as FT
TheFix =FT.Fix()
TheFix.setSightingFile()
approximateposition=TheFix.set_AriesFile()
print approximateposition
approximateposition=TheFix.set_StarFile()
print approximateposition
approximateposition=TheFix.get_Sightings()
print approximateposition
TheFix.calculate()
approximateposition=TheFix.raiseException()
print approximateposition