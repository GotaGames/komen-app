#no main.py
#no main.py
#pacotes de kivy
from kivy.app import App
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.utils import platform
from kivy.utils import platform
from kivy.uix.screenmanager import Screen
from plyer import filechooser, storagepath
from plyer import filechooser
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
#pacotes de codigo
import datetime
import random
import json, pathlib
from datetime import date
from avaliacoes import gerar_teste
import os
from plyer import notification
import datetime
import platform
import webbrowser
from kivy.storage.jsonstore import JsonStore


store = JsonStore("dados_usuario.json")

#FUNCIONALIDADES FLUTUANTES(FF)
#Motivacao
def obter_mensagem_motivacional():
    mensagens = [
        "Receba está motivação digna de campeões: «Seja qual for o seu sonho, comece. Ousadia tem genialidade, poder e magia.» – John Anster",
        "Está na hora de arrebentar mais um dia: «Motivação é o que te faz começar, hábito é o que faz você continuar.» – Jim Ryun",
        "#EU SOU O AUTOR DA MINHA VIDA: «Existe um momento na vida de cada pessoa em que é possível sonhar e realizar nossos sonhos... E esse momento tão fugaz chama-se presente e tem a duração do tempo que passa.» – Mario Quintana",
        "Palavras vencedoras logo ao iniciar o dia: «Não existem impossíveis quando o sonho comanda a vida. Acredite e lute.» – Desconhecido",
         "Pega visão: «Você é livre para fazer as suas escolhas, mas é prisioneiro das consequências.» – Pablo Neruda",
        "Bora despertar esse fire: «Enquanto você continuar respirando, Deus quer te dizer que a tua missão não acabou e tens ainda um potencial aí dentro.» – Desconhecido",
        "Topa mais um dia: «Uma semente, para que se transforme numa planta, precisa antes morrer. Todo o sucesso na vida exige sacrifício.» – Desconhecido",
        "Estou fervendo com essa de hoje: «O teu dia de hoje será definido pelos primeiros pensamentos e primeiras ações que tu tomares. O que escolhes? Ser um fracasso, ou um campeão?» – Desconhecido",
        "Essa é dura, yo: «Não é talento, não é sorte. O segredo do sucesso digno é a persistência e a autodisciplina.» – Desconhecido",
        "Escuta, guarda essa: «Se você se comprometeu a fazer algo, faça-o! O teu cérebro tem que aprender a trabalhar apesar da falta de entusiasmo, do medo e da incerteza.» – Desconhecido",
        "Aqui vai uma das mais maravilhosas: «O que você sonha é uma manifestação do que o teu eu do futuro está vivendo. O que ele te mostra?» – Desconhecido",
        "Engole essa com estilo😎: «Saiba o que você quer, trabalhe por isso, veja os resultados e troque a estratégia até você conseguir.» – Técnica do KFC",
        "Verdade como essa é digna de Motivação diária: «Esta é a tua vida. Não deixes que o teu lugar de protagonista seja roubado por pessoas, reclamações, vitimismo ou procrastinação.» – Desconhecido",
        "Vamos voar até onde?: «Nutra sua mente com grandes pensamentos, pois você nunca irá viver mais alto do que aquilo que você pensa.» – Benjamin Disraeli",
        "Hoje é um daqueles dias firesssss: «Tudo parece impossível até que seja feito.» – Nelson Mandela",
        "Diretamente de China: «A persistência realiza o impossível.» – Provérbio Chinês",
        "Cê é corajoso por batalhar todos os dias: «Coragem é a resistência ao medo, domínio do medo – não ausência do medo.» – Mark Twain",
        "Toca a acordar?: «A melhor maneira de prever o futuro é criá-lo.» – Peter Drucker",
        "Mais um clássico: «Grandes realizações nascem de grandes sacrifícios.» – Napoleon Hill",
        "É assim mesmooooo: «Transformei minha dor em arte porque era a única forma de continuar viva». – Frida Kahlo",
        "Nem todos os dias são bons:«Escrevo para não enlouquecer com o peso da minha existência.»– Virginia Woolf",
        "Sobre persistência, yo: «Perdi tudo, menos minha capacidade de tentar de novo.» – Nelson Mandela",
        "Tá pronto pro impacto?: «Você não é obrigado a vencer todos os dias, mas é obrigado a nunca desistir.»",
        "Receba essa flechada motivacional: «As grandes batalhas só são dadas aos grandes guerreiros.»",
        "Dá o play no foco: «A dor que você sente hoje será a força que você usará amanhã.»",
        "Essa é tapa na alma: «Não é sobre ser o melhor, é sobre ser melhor do que ontem.»",
        "Só vai: «O sucesso é construído nos dias em que você não quer levantar da cama.»",
        "Pra começar com tudo: «O mundo se cala diante de quem tem coragem de continuar.»",
        "Anota essa no peito: «Quem tem propósito não se distrai com o barulho do mundo.»",
        "Mano, segura essa visão: «Não tenha medo de crescer lentamente, tenha medo apenas de ficar parado.»",
        "Com essa aqui não tem como não agir: «A zona de conforto é bonita, mas nada cresce lá.»",
        "Vai explodir tua mente: «Não existe vitória sem disciplina. A vitória gosta de rotina.»",
        "Toma essa como soco de realidade: «Você não vai vencer na vida sendo gentil com seus próprios limites.»",
        "Já chega com sangue nos olhos: «A vontade de desistir é o teste final antes do teu próximo nível.»",
        "Palavras de aço: «Caminhar devagar ainda é melhor do que estar parado.»",
        "Puxa essa pro coração: «Você já sobreviveu a 100% dos seus piores dias. Você é forte!»",
        "Reflete nessa: «Quem espera que a sorte mude, nunca entendeu o poder da ação.»",
        "Clássica e poderosa: «Ninguém colhe sem plantar, ninguém vence sem lutar.»",
        "🔥🔥🔥: «A tua dor hoje é o preço da tua liberdade amanhã.»",
        "Motivação raiz: «Grandes conquistas exigem grandes versões de você.»",
        "Estilo guerreiro: «Não se trata de estar pronto, trata-se de começar mesmo com medo.»",
        "Essa é alma de campeão: «Você foi feito para ser extraordinário. Só precisa lembrar disso todos os dias.»",
        "Tira da mente e mete na prática: «A dúvida mata mais sonhos do que o fracasso jamais matará.»",
        "Mais quente que o sol: «Enquanto eles dormem, você treina. Enquanto eles descansam, você constrói.»",
        "Essa é faca no dente: «Você não precisa de mais motivação, você precisa de mais atitude.»",
        "Palavras que pulsam: «Não é sorte. É fé, suor, foco e ação.»",
        "Leve essa pra vida: «Cada passo certo te aproxima de um futuro onde você é imparável.»",
        "Pra chacoalhar: «Não espere que seja fácil, espere que valha a pena.»",
        "Pega a visão do topo: «Você não nasceu pra sobreviver, nasceu pra vencer.»",
        "Essa vale moldura: «Sonhos grandes assustam. Mas são esses que movem o mundo.»",
        "Daquelas que ficam: «A sua missão é maior que a sua preguiça.»",
        "Pra finalizar voando: «Você não precisa estar motivado todos os dias, você precisa ser disciplinado todos os dias.»",
        "Essa é de ouro: «Acredite em si próprio e chegará um dia em que os outros não terão outra escolha senão acreditar com você.» – Cynthia Kersey",
        "Reflexiva e certeira: «Não importa quão devagar você vá, desde que você não pare.» – Confúcio",
        "Essa vem com alma: «Você deve ser a mudança que deseja ver no mundo.» – Mahatma Gandhi",
        "Receba mais essa chama: «A única maneira de fazer um excelente trabalho é amar o que faz.» – Steve Jobs",
        "Forte e direta: «Só se pode alcançar um grande êxito quando nos mantemos fiéis a nós mesmos.» – Friedrich Nietzsche",
        "Explosiva: «Quando você quer alguma coisa, todo o universo conspira para que você realize o seu desejo.» – Paulo Coelho",
        "Clássica e elegante: «Tudo o que um sonho precisa para ser realizado é alguém que acredite que ele possa ser realizado.» – Roberto Shinyashiki",
        "Essa é pilar de mindset: «Não espere por uma crise para descobrir o que é importante na sua vida.» – Platão",
        "Estilo sabedoria ancestral: «Quem olha para fora, sonha. Quem olha para dentro, desperta.» – Carl Jung",
        "De quebrar correntes mentais: «A mente que se abre a uma nova ideia jamais voltará ao seu tamanho original.» – Albert Einstein",
        "Força silenciosa: «As maiores batalhas são travadas no silêncio da alma.»",
        "Profunda: «Se for pra desistir, desista de ser fraco.»",
        "Soco no sistema: «A vida é muito curta pra viver pequeno.» – Benjamin Disraeli",
        "Essa bate como muralha: «A coragem é saber que pode falhar, mas fazer mesmo assim.»",
        "Visão de águia: «Trabalhe até que seus ídolos se tornem seus rivais.»",
        "Mano, essa é pistão: «Nada floresce de um solo que você não rega.»",
        "Vem de cima: «Deus não te dá sonhos pequenos porque sabe que dentro de ti habita um gigante.»",
        "Pega essa chave: «As portas que você espera se abrirão quando você parar de bater e começar a construir as suas.»",
        "Filosofia na veia: «O homem que move montanhas começa carregando pequenas pedras.» – Provérbio chinês",
        "Sem freio: «Pare de se diminuir pra caber em lugares que você nasceu pra liderar.»",
        "Essa arrepia: «Você já tem o 'não'. Então vai atrás do 'sim'.»",
        "Topzera total: «Desistir? Só se for do medo.»",
        "Motivação blindada: «Não é sobre quem acredita em você. É sobre você acreditar quando ninguém mais acredita.»",
        "Tiro certo: «Cada pequeno progresso ainda é um progresso.»",
        "Estilo blindado: «Vão duvidar de ti até verem que não dá mais pra te ignorar.»",
        "Toma essa direto do front: «Lute com fé. A dor não é o fim, é só o processo.»",
        "Daquelas pra tatuar: «Quem ousa, às vezes cai. Mas quem não ousa já está no chão.»",
        "Essa é visão de rei: «O trono espera quem não abandona o campo de batalha.»",
        "Vem como fogo no peito: «Você tem uma escolha: continuar onde está ou ir atrás de quem nasceu pra ser.»",
        "Clássica e necessária: «Não tenha medo da perfeição — você nunca vai alcançá-la.» – Salvador Dalí",
        "Arrebatadora: «Às vezes, tudo o que você precisa é decidir que não vai desistir hoje.»",
        "Real e crua: «Se está difícil, é porque está funcionando.»",
        "Pra explodir o dia: «Não existe elevador pro sucesso. Você vai ter que subir pela escada.» – Zig Ziglar",
        "Toque de mestre: «Você não foi criado para se encaixar. Foi criado para se destacar.»",
        "Simples e letal: «Não reclame. Levante. Faça.»",
        "🔥 máxima: «Desafios não são obstáculos, são oportunidades disfarçadas.»",
        "Verdade nua e crua: «Enquanto você pensa em começar, alguém já começou com metade do que você tem.»",
        "Clássica de batalhador: «Não desista. Às vezes é a última chave no chaveiro que abre a porta.»",
        "Essa é coração de guerreiro: «Ser forte é continuar mesmo quando tudo em você grita por descanso.»",
        "Finalizando com rajada: «Você não veio até aqui pra ser quase.»"

    ]
    
    hoje = datetime.date.today()
    random.seed(hoje.toordinal())
    return random.choice(mensagens)


    
    
#FUNCIONALIDADES COM TELA
#TAREFAS
DATA = pathlib.Path("tarefas_data.json")
def _carregar():
    if DATA.exists():
        return json.loads(DATA.read_text())
        return {}
        
def _salvar(info):
    DATA.write_text(json.dumps(info, indent=2))

def obter_hoje():
    return str(date.today())
   
def salvar_resultado_do_dia(pontos, total):
    dados = _carregar() or {}
    hoje = obter_hoje()
    dados.setdefault("dias",{})[hoje] = {"pontos": pontos, "total": total}
    _salvar(dados)
    
def resumo_semana():
    dados = _carregar().get("dias", {})
    dias = sorted(dados.keys())[-14:]
    semana_atual = dias[-7:]
    semana_passada = dias[:-7]
    if not dados:
        return 0.0, 0.0
    def media(lst):
        return sum(dados[d]["pontos"]/dados[d]["total"] for d in lst)/len(lst) if list else 0
        return media(semana_atual), media(semana_passada)
        
    

# Telas
class MenuScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.atualizar_motivacao, 0.1)

    def atualizar_motivacao(self, dt):
        mensagem = obter_mensagem_motivacional()
        self.ids.label_motivacao.text= mensagem
 #TELAS
class PerfilScreen(Screen):
    def on_pre_enter(self):
        Clock.schedule_once(self.carregar_dados, 0.1)

    def carregar_dados(self, *args):
        self.ids.conteudo.clear_widgets()

        if store.exists("usuario"):
            dados = store.get("usuario")
            campos = [
                ("👤 Nome completo", dados.get("nome", "")),
                ("📧 Email", dados.get("email", "")),
                ("🔖 Apelido", dados.get("apelido", "")),
                ("📘 Curso", dados.get("curso", "")),
                ("📅 Início do Semestre", dados.get("inicio", "")),
                ("📅 Fim do Semestre", dados.get("fim", "")),
                ("🎯 Meta", dados.get("meta", "")),
                ("⭐ Disciplinas prioritárias", dados.get("prioritarias", "")),
                ("⏳ Estuda com o Komen desde", dados.get("estudando_desde", "")),
                ("💬 Frase de inspiração", dados.get("inspiracao", ""))
            ]

            for titulo, valor in campos:
                self.ids.conteudo.add_widget(Label(text=f"{titulo}: {valor}"))
        else:
            self.ids.conteudo.add_widget(Label(text="Nenhum dado encontrado."))
            

            
            


class DesempenhoScreen(Screen): 
    pass


class DefinicoesScreen(Screen):
    pass

class MyApp(App):
    nomes_agradecimento = ["Ione Kathy"]

    def on_start(self):
        definicoes = store.get("definicoes") if store.exists("definicoes") else {}

        # Aplica as definições ao abrir o app
        try:
            self.root.get_screen("definicoes").ids.switch_notificacoes.active = definicoes.get("notificacoes", True)
            self.root.get_screen("definicoes").ids.switch_escuro.active = definicoes.get("tema_escuro", False)
            self.root.get_screen("definicoes").ids.spinner_fonte.text = definicoes.get("fonte", "Médio")
        except Exception as e:
            print("Erro ao aplicar definições:", e)
        


    # ---- Aparência ----
    def toggle_tema(self, escuro):
        print("Modo escuro?", escuro)
        if not store.exists("definicoes"):
            store.put("definicoes", tema_escuro=escuro)
        else:
            store.put("definicoes", **{**store.get("definicoes"), "tema_escuro": escuro})

        # TODO: implementar troca de tema

    def ajustar_fonte(self, tamanho):
        print("Fonte escolhida:", tamanho)
        if not store.exists("definicoes"):
            store.put("definicoes", fonte=tamanho)
        else:
            store.put("definicoes", **{**store.get("definicoes"), "fonte": tamanho})
        # TODO: aplicar tamanho global

    # ---- Notificações ----
    def config_notificacoes(self, ativado):
        print("Notificações ativas?", ativado)
        if not store.exists("definicoes"):
            store.put("definicoes", notificacoes=ativado)
        else:
            store.put("definicoes", **{**store.get("definicoes"), "notificacoes": ativado})
        # TODO: ligar/desligar agendamentos quando criar o sistema real

    # ---- Agradecimentos ----
    def adicionar_nome_agradecimento(self):
        novo_nome = "Novo Nome"
        self.nomes_agradecimento.append(novo_nome)
        lista = "\n• " + "\n• ".join(self.nomes_agradecimento)
        self.root.get_screen("definicoes").ids.label_agradecimentos.text = f"Agradecimentos eternos a:{lista}"

    # ---- Ajuda e suporte ----
    def abrir_manual(self):
        print("Abrir PDF/manual")

    def enviar_feedback(self):
        print("Abrir e-mail para feedback")

    def contato_suporte(self):
        print("Mostrar contato de suporte")




class TarefasScreen(Screen): 
    tarefas_diarias = ListProperty([]) #lista de strings
    def on_enter(self):
        Clock.schedule_once(self._atualizar_ui, 0.1)
    
    def adicionar_tarefa(self):
        texto = self.ids.input_tarefa.text.strip()
        if not texto:
            return
        self.tarefas_diarias.append({"texto": texto, "feito": None, "motivo": ""})
        self.ids.input_tarefa.text = ""
        self._atualizar_ui()

    def _atualizar_ui(self, dt=None):
        box = self.ids.lista_tarefas_box
        box.clear_widgets()
        for t in self.tarefas_diarias:
            lbl = Label(
                text="☐ " + t["texto"],
                size_hint_y=None,
                height=30,
                halign="left",
                valign="middle",
                text_size=(self.width, None)
            )
            box.add_widget(lbl)

    def iniciar_avaliacao(self):
        if not self.tarefas_diarias:
            self._popup("Nenhuma tarefa para hoje.")
            return 
        self._avaliar_indice(0, 0)

    def _avaliar_indice(self, idx, pontos):
        if idx >= len(self.tarefas_diarias):
            total = len(self.tarefas_diarias)
            salvar_resultado_do_dia(pontos, total)
            resultado = resumo_semana()
            if resultado is None:
                media_atual = media_passada = 0.0
            else:
                media_atual, media_passada = resultado
            
            msg = f"Concluído!\nPontuação de hoje: {pontos}/{total} = {pontos/total:.0%}\n\nSemana atual: {media_atual:.0%}\nSemana passada: {media_passada:.0%}"
            self._popup(msg)
            self.tarefas_diarias = []
            self._atualizar_ui()
            return

        t = self.tarefas_diarias[idx]
        p = Popup(title=f"Tarefa {idx+1}", size_hint=(.8, .4))
        box = BoxLayout(orientation="vertical", spacing=10, padding=10)
        box.add_widget(Label(text=t["texto"], halign="center"))
        btns = BoxLayout(size_hint_y=None, height=40, spacing=10)
        btn_sim = Button(text="Cumpri ✅")
        btn_nao = Button(text="Não cumpri ❌")
        btns.add_widget(btn_sim)
        btns.add_widget(btn_nao)
        box.add_widget(btns)
        p.content = box

        def on_sim(instance):
            self.tarefas_diarias[idx]["feito"] = True
            p.dismiss()
            self._avaliar_indice(idx + 1, pontos + 1)

        def on_nao(instance):
            self.tarefas_diarias[idx]["feito"] = False
            p.dismiss()
            self._perguntar_motivo(idx, pontos)

        btn_sim.bind(on_release=on_sim)
        btn_nao.bind(on_release=on_nao)
        p.open()

    def _perguntar_motivo(self, idx, pontos):
        p = Popup(title="O que falhou?", size_hint=(.8, .5))
        box = BoxLayout(orientation="vertical", spacing=10, padding=10)
        motivo_input = TextInput(hint_text="Escreve aqui…")
        ok_btn = Button(text="OK", size_hint_y=None, height=40)

        def salvar_motivo(instance):
            self.tarefas_diarias[idx]["motivo"] = motivo_input.text
            p.dismiss()
            self._avaliar_indice(idx + 1, pontos)

        ok_btn.bind(on_release=salvar_motivo)
        box.add_widget(motivo_input)
        box.add_widget(ok_btn)
        p.content = box
        p.open()

    def _popup(self, msg):
        Popup(title="Info", content=Label(text=msg), size_hint=(.8, .4)).open()


#Resumos yo
CAMINHO_RESUMOS = os.path.join(os.getcwd(), "resumos_komen")

class ResumosScreen(Screen):

    def on_enter(self):
        self._criar_pasta_resumos()
        self._verificar_permissoes()
        Clock.schedule_once(lambda dt: self.mostrar_resumos())

    def _criar_pasta_resumos(self):
        if not os.path.exists(CAMINHO_RESUMOS):
            os.makedirs(CAMINHO_RESUMOS)

    def _verificar_permissoes(self):
        if platform == 'android':
            from plyer import permission
            permission.request('android.permission.READ_EXTERNAL_STORAGE')
            permission.request('android.permission.WRITE_EXTERNAL_STORAGE')

    def escolher_arquivo(self):
        def selecionar(caminhos):
            if caminhos:
                caminho = caminhos[0]
                nome = os.path.basename(caminho)
                destino = os.path.join(CAMINHO_RESUMOS, nome)

                # Copia o arquivo para a pasta local do app
                try:
                    with open(caminho, 'rb') as origem, open(destino, 'wb') as novo:
                        novo.write(origem.read())
                    self.mostrar_resumos(self, dt)
                    self.notificar("Nova Avaliação Disponível", "Baseado no novo resumo enviado.")
                except Exception as e:
                    print("Erro ao copiar arquivo:", e)

        if platform == 'android':
            filechooser.open_file(on_selection=selecionar)
        else:
            filechooser.open_file(on_selection=selecionar)
        

    def on_enter(self):
        Clock.schedule_once(self.mostrar_resumos, 0.1)

    def mostrar_resumos(self,dt):
        box = self.ids.box_resumos
        box.clear_widgets()

        arquivos = os.listdir(CAMINHO_RESUMOS)
        if not arquivos:
            from kivy.uix.label import Label
            box.add_widget(Label(text="Nenhum resumo carregado."))
            return

        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.uix.popup import Popup

        for arquivo in arquivos:
            from kivy.graphics import Color, RoundedRectangle
            card = BoxLayout(
                orientation='horizontal',
                padding=10,
                spacing=5,
                size_hint_y=None,
                height=60
            )

            with card.canvas.before:
                Color(1, 1, 1, 1)  # Branco puro (R,G,B,Alpha)
                card.fundo = RoundedRectangle(
                    pos=card.pos,
                    size=card.size,
                    radius=[12]
                )

            # Atualizar posição/tamanho quando o layout mudar
            card.bind(pos=lambda instance, value: setattr(card.fundo, 'pos', value))
            card.bind(size=lambda instance, value: setattr(card.fundo, 'size', value))


            
            
            card.canvas.before.clear()

            nome_label = Label(text=arquivo, size_hint_y=None, height=30)

                # Botão de opções (três pontinhos)
            menu_btn = Button(text='⋮', size_hint=(None, None), size=(30, 30), pos_hint={"right": 1})

            def mostrar_menu(instance, nome=arquivo):
                content = BoxLayout(orientation='vertical', spacing=5, padding=10)
                popup = Popup(title=f"Opções para {nome}", content=content, size_hint=(None, None), size=(300, 300))

                btn_avaliar = Button(text='📊 Avaliação')
                btn_renomear = Button(text='✏️ Mudar Nome')
                btn_deletar = Button(text='🗑️ Eliminar')

                def abrir_ficheiro(x):
                    caminho_arquivo = os.path.join(CAMINHO_RESUMOS, nome)

                    extensao = os.path.splitext(caminho_arquivo)[1].lower()
                    conteudo = ""

                    try:
                        if extensao == ".txt":
                            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                                conteudo = f.read()

                        elif extensao == ".pdf":
                            try:
                                import fitz  # PyMuPDF
                                doc = fitz.open(caminho_arquivo)
                                for page in doc:
                                    conteudo += page.get_text()
                                doc.close()
                            except ImportError:
                                conteudo = "[Erro] Biblioteca 'fitz' não instalada"

                        elif extensao == ".docx":
                            try:
                                import docx
                                doc = docx.Document(caminho_arquivo)
                                for para in doc.paragraphs:
                                    conteudo += para.text + "\n"
                            except ImportError:
                                conteudo = "[Erro] Biblioteca 'python-docx' não instalada"

                        else:
                            conteudo = "Formato não suportado."

                    except Exception as e:
                        conteudo = f"[Erro ao abrir]: {str(e)}"

                    # Mostrar o conteúdo num popup
                    scroll = ScrollView()
                    texto = Label(text=conteudo, size_hint_y=None, text_size=(280, None))
                    texto.bind(texture_size=texto.setter("size"))
                    scroll.add_widget(texto)

                    popup_resultado = Popup(title=f"📖 {nome}", content=scroll,
                                            size_hint=(None, None), size=(320, 400))
                    popup_resultado.open()
                    popup.dismiss()


                def avaliar_resumo(x):
                    app = App.get_running_app()
                    app.root.current = "avaliacao"
                    app.root.get_screen("avaliacao").selecionar_resumo(nome)
                    popup.dismiss()

                def renomear_resumo(x):
                    novo_nome = nome.replace(".txt", "_novo.txt")  # Simples, pode usar popup depois
                    os.rename(os.path.join(CAMINHO_RESUMOS, nome), os.path.join(CAMINHO_RESUMOS, novo_nome))
                    self.mostrar_resumos(0)
                    popup.dismiss()

                def deletar_resumo(x):
                    os.remove(os.path.join(CAMINHO_RESUMOS, nome))
                    self.mostrar_resumos(0)
                    popup.dismiss()

                btn_abrir = Button(text='📂 Abrir Ficheiro')
                btn_abrir.bind(on_release=abrir_ficheiro)
                btn_avaliar.bind(on_release=avaliar_resumo)
                btn_renomear.bind(on_release=renomear_resumo)
                btn_deletar.bind(on_release=deletar_resumo)

                content.add_widget(btn_abrir)
                content.add_widget(btn_avaliar)
                content.add_widget(btn_renomear)
                content.add_widget(btn_deletar)
                popup.open()

            menu_btn.bind(on_release=mostrar_menu)

                # Container do card
            card.add_widget(nome_label)
            card.add_widget(menu_btn)
            box.add_widget(card)


            

        
            
            


class AvaliacaoScreen(Screen):
    def selecionar_resumo(self, nome_arquivo):
        from assets.funcionalidades.avaliacoes import gerar_teste
        caminho = os.path.join(CAMINHO_RESUMOS, nome_arquivo)

        # Pega o valor do Spinner e extrai o número da dificuldade
        nivel_bruto = self.ids.spinner_dificuldade.text
        try:
            nivel = int(nivel_bruto.split("-")[0].strip())
        except:
            nivel = 1  # Valor padrão se der erro

        # Gera as perguntas com base no caminho e dificuldade
        perguntas = gerar_teste(caminho, dificuldade=nivel)

        # Limpa e exibe as perguntas e campos de resposta
        self.ids.area_perguntas.clear_widgets()
        for pergunta in perguntas:
            label = Label(
                text=f"❓ {pergunta}",
                size_hint_y=None,
                text_size=(self.ids.area_perguntas.width, None),
                halign='left',
                valign='top'
    )
    # Faz o label crescer conforme o texto
            label.bind(
                width=lambda instance, value: setattr(instance, 'text_size', (value, None)),
                texture_size=lambda instance, value: setattr(instance, 'height', value[1])
            )
            self.ids.area_perguntas.add_widget(label)

            self.ids.area_perguntas.add_widget(TextInput(
                hint_text="📝 Sua resposta...",
                size_hint_y=None,
                height=100
            ))         
    def submeter_respostas(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text="✅ A sua avaliação foi submetida com sucesso!", halign="center"))

        btn_fechar = Button(text="Fechar", size_hint_y=None, height=40)
        layout.add_widget(btn_fechar)

        popup = Popup(title="Avaliação Submetida",
                      content=layout,
                      size_hint=(None, None),
                      size=(300, 200),
                      auto_dismiss=False)

        btn_fechar.bind(on_release=popup.dismiss)
        popup.open()
                         






class NotificacoesScreen(Screen): 
    pass
class ComunidadeScreen(Screen): 
    pass

# Gerenciador de telas
class KomenGerenciador(ScreenManager): 
   pass

# App principal
class KomenApp(App):
    hora_estudo = "19:00"  # Exemplo: hora definida pelo usuário no início da sessão (formato HH:MM)
    


    def build(self):
        Builder.load_file("komen.kv")
        Clock.schedule_once(self.iniciar_agendamentos, 1)
        return KomenGerenciador()
        


    def iniciar_agendamentos(self, *args):
        # Missão do dia às 5h da manhã
        Clock.schedule_interval(self.checar_missao_do_dia, 60)  # Checa a cada minuto

        # Lembrete de água a cada 2h
        Clock.schedule_interval(self.notificar_beber_agua, 60 * 60 * 2)

        # Checagem de hora favorável para estudo a cada minuto
        Clock.schedule_interval(self.checar_hora_estudo, 60)

    def notificar(self, titulo, mensagem):
        try:
            if self.plataforma in ["Linux", "Windows", "Darwin"]:  # Darwin = macOS
                notification.notify(
                    title=titulo,
                    message=mensagem,
                    timeout=10
                )
            elif self.plataforma == "Android":
                try:
                    from plyer import notification
                    notification.notify(
                        title=titulo,
                        message=mensagem,
                        timeout=10
                    )
                except Exception as e:
                    print("Erro ao notificar no Android:", e)
            else:
                print("Plataforma não suportada para notificações:", self.plataforma)
        except Exception as e:
            print("Erro ao tentar notificar: ", e)

        
    def on_start(self):
        self.plataforma = platform.system()
        self.hora_estudo = "14:00"  # ou carregar de config
        self.iniciar_agendamentos()




    def checar_hora_estudo(self, dt):
        agora = datetime.datetime.now().strftime("%H:%M")
        if agora == self.hora_estudo:
            self.notificar("Hora de Estudar", "Lembrete: é a tua hora favorita para estudar!")
        elif agora > self.hora_estudo:
            self.notificar("Faltou Estudo?", "Já passou a hora de estudar... Tudo bem, ainda dá tempo!")

    def checar_missao_do_dia(self, dt):
        agora = datetime.datetime.now().strftime("%H:%M")
        if agora == "05:00":
            self.notificar("Missão do Dia", "Tua missão está pronta! Vamos nessa, herói do Komen 💥")

    def notificar_beber_agua(self, dt):
        self.notificar("Hidratação 💧", "Hora de beber água e dar uma pausa rápida.")

    def abrir_manual(self):
        # Substitua com o link real do seu manual (pode ser um PDF no Google Drive, por exemplo)
        link_manual = "https://gotagames.github.io/Komen-menu/"
        webbrowser.open(link_manual)

    def enviar_feedback(self):
        email = "gotagames.co@gmail.com"
        assunto = "Feedback sobre o app"
        corpo = "Olá Gota Games, gostaria de compartilhar o seguinte feedback..."
        link_email = f"mailto:{email}?subject={assunto}&body={corpo}"
        webbrowser.open(link_email)

    def contato_suporte(self):
        numero = "258864573666"  # Substituir com seu número real
        mensagem = "Olá! Preciso de suporte com o app Komen."
        link_whatsapp = f"https://wa.me/{numero}?text={mensagem}"
        webbrowser.open(link_whatsapp)


    

#iniciar o app
    def build(self):
        
        return Builder.load_file("komen.kv")

        
#funcionalidade para resetar processo/terminar funcao
    def resetar_processo(self):
        print("🔁 Resetando processo do usuário... (aqui vai a lógica depois)")

    def terminar_sessao(self):
        print("🚪 Sessão terminada. (aqui vai a lógica de logout depois)")

    


if __name__ == "__main__":
    KomenApp().run()








