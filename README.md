Projeto de Sistema de Registro de Ponto com Reconhecimento Facial
1. Objetivo do Sistema

O sistema tem como objetivo automatizar o registro de entrada e saída de funcionários em empresas através de reconhecimento facial, promovendo precisão e segurança. A solução visa simplificar a gestão de presença e integrar-se aos sistemas administrativos existentes.

2. Componentes do Sistema

Ambiente de Desenvolvimento:

Python: Linguagem utilizada para o desenvolvimento do sistema devido à sua simplicidade e vasta gama de bibliotecas.
Visual Studio Code (VSCode): IDE escolhida para a escrita e depuração do código, oferecendo uma interface intuitiva e suporte a extensões úteis.

Tecnologias e Bibliotecas:

OpenCV: Biblioteca utilizada para captura e processamento de vídeos, essencial para o reconhecimento facial.
Face Recognition: Baseada em dlib, esta biblioteca realiza a identificação facial com alta precisão.
SQLite: Banco de dados escolhido por sua leveza e facilidade de uso, utilizado para armazenamento de dados.
smtplib: Parte da biblioteca padrão do Python, utilizada para o envio de e-mails de confirmação de ponto.

Estrutura do Projeto:

main.py: Arquivo principal que integra os componentes do sistema.
database.py: Gerencia a criação e interação com o banco de dados de colaboradores.
reconhecimento_facial.py: Responsável pela captura de vídeo e execução do reconhecimento facial.
envio_email.py: Concentra funções para envio de e-mails.
face_recognition.py: Responsável pelo reconhecimento facial dos colaboradores registrados.
Diretório imagens_referencia/: Armazena imagens de referência usadas no reconhecimento facial.


3. Processo de Desenvolvimento

Configuração do Ambiente: Configuração do ambiente virtual Python para gerenciamento de dependências e instalação de bibliotecas via pip, como opencv-python e face_recognition.

Desenvolvimento do Banco de Dados: Criação do banco colaboradores.db usando SQLite, contendo rotinas para cadastro de colaboradores com informações básicas como nome, e-mail e imagem de referência.

Implementação do Reconhecimento Facial: Uso do OpenCV para captura e manipulação de dados da webcam, e da biblioteca Face Recognition para detecção e verificação de rostos.

Integração de Envio de E-mail: Configuração do envio de e-mails via smtplib, estabelecendo conexão segura com o servidor SMTP para comunicação com os usuários após o registro de ponto.

Testes e Validações: Realização de testes unitários e de integração para garantir a robustez e a segurança do sistema, com ajustes conforme necessário.

4. Considerações Finais

O sistema foi concebido para ser escalável e passível de integração com outros sistemas de gestão empresarial, oferecendo não apenas precisão e segurança no registro de presenças, mas também um meio moderno de comunicação com os colaboradores.

