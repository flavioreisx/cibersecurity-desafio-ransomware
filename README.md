# Criando um Ransomware com Python

### Ferramentas

- Python

### Criptografando os dados
Aqui vamos criar um arquivo chamado encrpterAll.py com o código para criptografa os arquivos na pasta corrente, utilizando chave de criptografia 32 bytes, na saída do executravél vai retornar a informação quais arquivos foram criptografados e o total.

![image](https://github.com/user-attachments/assets/2c839392-9737-4c5d-ac1c-0cfcf113147f)




### Descriptografando os dados
Nesse arquivo chamado descrypterAll.py vamos inserir o código para descriptografar os arquivos criptografados na pasta corrente, utilizando a mesma chave de 32 bytes, na saída do executravél vai retornar a informação quais arquivos foram removidos a criptografia e o total.

![image](https://github.com/user-attachments/assets/21b014a7-5401-4199-9e3f-2c04153a7420)




### Realizando Teste


- listando os arquivos dentro do diretório e visualizando o conteúdo do arquivo sem criptografia.

![image](https://github.com/user-attachments/assets/bfb0617c-523d-4926-9fea-eb97ba40ceb0)

### Criptografando os arquivos

- Executando o arquivo encypterAll.py que vai criptografar todos os arquivos na pasta corrente.
- Ao finalizar vai mostrar a mensagem que "Todos os arquivos foram Criptografados com Sucesso!" e vai informar o total de arquivos criptografos no final.

![image](https://github.com/user-attachments/assets/4b718451-de8b-4ec3-8f13-d655903a025d)



### Visualizando os arquivos criptografados

Quando um arquivo é criptografado, seus dados são transformados em uma forma ilegível usando um algoritmo de criptografia e uma chave secreta. O processo embaralha os dados originais, tornando-os inacessíveis sem a chave correta. O arquivo criptografado é armazenado de forma segura, protegendo seu conteúdo. Somente quem possui a chave correta pode descriptografar e acessar os dados originais.

Podemos observar que todos os arquivos estão conforme a visualização do arquivo abaixo.

- Visualizando o arquivo TXT utilizando o cat
  
![image](https://github.com/user-attachments/assets/7bac27b7-46ad-44b5-bdc3-5b34a86a0202)


- Visualizando no VIM
  
![image](https://github.com/user-attachments/assets/e99d4f68-ae66-417d-9615-0092f2d3deba)


### Descriptografando os arquivos

- Executando nosso arquivo decrypterAll.py
- Recebemos a informação que "Todos os arquivos foram Descriptografados com Sucesso!"

![image](https://github.com/user-attachments/assets/29a2a1a6-9742-4032-b145-b5b0188b073d)




### Visualizando os arquivos descriptografados


- Visualizando o arquivo TXT utilizando o cat

![image](https://github.com/user-attachments/assets/84dfe17b-a668-4814-a20b-0d051508e026)


Finalizado Desafio cybersecurity ransonware. 
