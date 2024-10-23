import streamlit as st

class Barragem:
    def __init__(self, volume, impacto_ambiental, perda_vidas, impacto_economico, conservacao, plano_seguranca):
        self.volume = volume
        self.impacto_ambiental = impacto_ambiental
        self.perda_vidas = perda_vidas
        self.impacto_economico = impacto_economico
        self.conservacao = conservacao
        self.plano_seguranca = plano_seguranca

    def classificar_volume(self):
        if self.volume <= 500_000:
            return "Muito Pequeno"
        elif 500_000 < self.volume <= 5_000_000:
            return "Pequeno"
        elif 5_000_000 < self.volume <= 25_000_000:
            return "Médio"
        elif 25_000_000 < self.volume <= 50_000_000:
            return "Grande"
        else:
            return "Muito Grande"

    def classificar_dano_potencial(self):
        # A pontuação do dano potencial associado considera impacto ambiental, perda de vidas e impacto econômico
        pontos = self.impacto_ambiental + self.perda_vidas + self.impacto_economico
        if pontos <= 7:
            return "Baixo"
        elif 7 < pontos <= 13:
            return "Médio"
        else:
            return "Alto"

    def classificar_risco(self):
        # A classificação do risco considera a conservação da barragem e o atendimento ao plano de segurança
        pontos_conservacao = self.conservacao
        pontos_plano_seguranca = self.plano_seguranca
        total_risco = pontos_conservacao + pontos_plano_seguranca
        if total_risco <= 10:
            return "Baixo"
        elif 10 < total_risco <= 19:
            return "Médio"
        else:
            return "Alto"

    def classificar_barragem(self):
        classificacao_volume = self.classificar_volume()
        classificacao_dano = self.classificar_dano_potencial()
        classificacao_risco = self.classificar_risco()
        
        return {
            "Classificação por Volume": classificacao_volume,
            "Classificação por Dano Potencial Associado": classificacao_dano,
            "Classificação por Categoria de Risco": classificacao_risco
        }

# Interface com Streamlit
st.title("Classificação de Barragens")

volume = st.number_input("Volume da barragem (em m³)", min_value=0.0, step=1.0)
impacto_ambiental = st.slider("Pontuação do Impacto Ambiental (0 a 10)", 0, 10, 0)
perda_vidas = st.slider("Pontuação da Perda de Vidas (0 a 10)", 0, 10, 0)
impacto_economico = st.slider("Pontuação do Impacto Econômico (0 a 10)", 0, 10, 0)
conservacao = st.slider("Estado de Conservação da Barragem (0 a 10)", 0, 10, 0)
plano_seguranca = st.slider("Atendimento ao Plano de Segurança (0 a 10)", 0, 10, 0)

if st.button("Classificar Barragem"):
    barragem = Barragem(volume, impacto_ambiental, perda_vidas, impacto_economico, conservacao, plano_seguranca)
    resultado = barragem.classificar_barragem()
    st.write("### Resultados da Classificação:")
    st.write(resultado)
