from sqlalchemy.inspection import inspect

class Serializer(object):
	excluded_columns=[]

	def serialize(self):
		return {c: getattr(self, c) for c in inspect(self).attrs.keys() if not c in self.excluded_columns}

	def toData(self):
		return [getattr(self, c) for c in inspect(self).attrs.keys() if not c in self.excluded_columns]

	def gethead(self):
		return [[c for c in inspect((self)).attrs.keys() if not c in self.excluded_columns]]
	@staticmethod
	def serialize_list(l):
		return [m.serialize() for m in l]

	@staticmethod
	def data_list(l):
		if len(l)<1:
			return ['']
			# data = 
		data=l[0].gethead()
		data.extend([m.toData() for m in l])
		return data
