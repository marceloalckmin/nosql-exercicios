from database import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

db = Database(database="Ex_Av1", collection="Motoristas")

motorista_dao = MotoristaDAO(db)

moto_CLI = MotoristaCLI(motorista_dao)
moto_CLI.run()