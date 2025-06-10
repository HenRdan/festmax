from django.db import models
from core.models import BaseModel, EnderecoModel
from core.choices import STATUS_PEDIDO_CHOICES, FORMA_PAGAMENTO_CHOICES, STATUS_PAGAMENTO_CHOICES, STATUS_ENTREGA_CHOICES

from accounts.models import Cliente

from products.models import Produto


class Pedido(BaseModel):
    """
    Modelo para representar um pedido de compra.
    """
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status_pedido = models.CharField(
        max_length=20, choices=STATUS_PEDIDO_CHOICES)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(
        max_length=20, choices=FORMA_PAGAMENTO_CHOICES)
    endereco_entrega = models.ForeignKey(
        EnderecoModel, on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-criacao']

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"


class ItemPedido(BaseModel):
    """
    Modelo para representar um item de pedido de compra.
    """
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'ItemPedido'
        verbose_name_plural = 'ItensPedido'
        ordering = ['-criacao']

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"ItemPedido {self.id} - {self.produto.nome}"


class Pagamento(BaseModel):
    """
    Modelo para representar um pagamento de pedido.
    """
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    status_pagamento = models.CharField(
        max_length=10, choices=STATUS_PAGAMENTO_CHOICES)
    forma_pagamento = models.CharField(
        max_length=10, choices=FORMA_PAGAMENTO_CHOICES)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-criacao']

    def __str__(self):
        return f"Pagamento {self.id} - {self.pedido.cliente.nome}"


class Entrega(BaseModel):
    """
    Modelo para representar uma entrega de pedido.
    """
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(
        EnderecoModel, on_delete=models.CASCADE)
    status_entrega = models.CharField(
        max_length=10, choices=STATUS_ENTREGA_CHOICES)
    data_prevista_entrega = models.DateField()
    codigo_rastreio = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'
        ordering = ['-criacao']

    def __str__(self):
        return f"Entrega {self.id} - {self.pedido.cliente.nome}"
