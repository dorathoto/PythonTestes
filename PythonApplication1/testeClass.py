from ContaBancaria import Cliente
from ContaBancaria import Conta
leo = Cliente('Leonardo', '4411-1194')
maria = Cliente('Maria','44555888')

conta1 = Conta(leo, 1,1000)
conta2 = Conta([leo, maria],2,500)
conta1.resumo()
conta2.resumo()
