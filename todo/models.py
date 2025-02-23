from django.db import models

class Todo(models.Model):
  nome = models.CharField(max_length=255)
  descricao = models.CharField(max_length=255)
  created_date = models.DateField(auto_now_add=True)
  data_limite = models.DateField()
  status = models.BooleanField()

  def __str__(self) -> str:
    status_text = 'Feita' if self.status else 'Não feita'
    return f"Nome: {self.nome.capitalize()} | Status: {status_text} | Data Criada : {self.created_date.strftime('%B %d, %Y')} | Data Limite: {self.data_limite.strftime('%B %d, %Y')}"