from django.db import models


class Tipo_Equipamento(models.Model):
    '''Modelo de Equipamentos'''
    tipo_equipamento = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo_equipamento


class Modelos(models.Model):
    '''Modelo de PC'''
    equipamento = models.ForeignKey(Tipo_Equipamento, on_delete=models.CASCADE)
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.modelo


class Ativos_TI(models.Model):
    '''Modelo de Computadores.'''

    memoria_choices = (
    ('2GB', '2GB'),
    ('3GB', '3GB'),
    ('4GB', '4GB'),
    ('6GB', '6GB'),
    ('8GB', '8GB'),
    ('16GB', '16GB'),
    ('32GB', '32GB'),
    )

    hd_choices = (
    ('240GB', '240GB'),
    ('250GB', '250GB'),
    ('500GB', '500GB'),
    ('1000GB', '1000GB'),
    ('2000GB', '2000GB'),
    ('SSD 240GB', 'SSD 240GB'),
    )

    so_choices = (
    ('Windows XP Profissional', 'Windows XP Profissional'),
    ('Windows 7 Home', 'Windows 7 Home'),
    ('Windows 7 Profissional', 'Windows 7 Profissional'),
    ('Windows 7 Ultimate', 'Windows 7 Ultimate'),
    ('Windows 8', 'Windows 8'),
    ('Windows 10 Profissional', 'Windows 10 Profissional'),
    )

    status_choices = (
    ('Ativo', 'Ativo'),
    ('Inativo', 'Inativo'),
    ('Manutenção', 'Manutenção'),
    )

    tipo = models.ForeignKey(Tipo_Equipamento, on_delete=models.CASCADE)
    tombamento = models.IntegerField(unique=True)
    numero_serie = models.CharField(max_length=100, unique=True)
    sistema_oper = models.CharField(max_length=50, blank=True, null=True, choices=so_choices, default='Windows 10 Profissional')
    licenca_so = models.CharField(max_length=100, blank=True, null=True, unique=True)
    ip = models.GenericIPAddressField(unique=True,blank=True, null=True)
    mac = models.CharField(max_length=50, blank=True, null=True, unique=True)
    processador = models.CharField(max_length=30, blank=True, null=True)
    memoria = models.CharField(max_length=4, blank=True, null=True, choices=memoria_choices, default='4GB')
    hd = models.CharField(max_length=10, blank=True, null=True, choices=hd_choices, default='500GB')
    status = models.CharField(max_length=11, choices=status_choices, default='Ativo')
    # setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelos, on_delete=models.CASCADE)
    vinculo_pc = models.IntegerField(blank=True, null=True)
    usuario_principal = models.CharField(max_length=50, blank=True, null=True)
    senha_wifi = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.numero_serie


class Manutencao(models.Model):
    """Modelo para Cadastro das Manutenções """
    equipamento = models.ForeignKey(Ativos_TI, on_delete=models.CASCADE)
    data_manutencao = models.DateTimeField(auto_now_add=True)
    manutencao = models.TextField(max_length=4096)

    def __str__(self):
        return self.manutencao
