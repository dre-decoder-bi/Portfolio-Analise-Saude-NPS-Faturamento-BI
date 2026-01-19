import pandas as pd
import numpy as np
import os

caminho_arquivo_original = r"coloque o seu caminho aqui"

print("Lendo arquivo original...")
df_real = pd.read_excel(caminho_arquivo_original)


tabela_precos = {
    'ALERGOLOGISTA': 250,
    'CARDIOLOGISTA': 300,
    'CIRURGIA GERAL': 300,
    'CIRURGIA PEDIATRICA': 350,
    'CLINICA MEDICA': 150,
    'COLONOSCOPIA': 700,
    'COLOPROCTOLOGISTA': 300,
    'COLPOSCOPIA': 250,
    'DERMATOLOGISTA': 250,
    'ECOCARDIOGRAMA': 350,
    'ENDOCRINOLOGISTA': 280,
    'ENDOSCOPIA': 500,
    'ENFERMAGEM PROCEDIMENTOS': 80,
    'ESPIROMETRIA': 150,
    'FONOAUDIOLOGIA': 120,
    'GASTROENTEROLOGISTA': 280,
    'GINECOLOGISTA': 280,
    'HEPATOLOGIA': 300,
    'HOLTER MAPEAMENTO': 200,
    'MAPA': 200,
    'MASTOLOGISTA': 300,
    'N/I': 0,
    'NEFROLOGIA': 300,
    'NEUROLOGIA': 320,
    'NEUROLOGIA PROCEDIMENTO': 200,
    'NEUROPEDIATRIA': 350,
    'NUTRICIONISTA': 150,
    'ODONTOLOGIA': 200,
    'OFTALMOLOGISTA': 250,
    'ORTOPEDISTA': 280,
    'OTORRINOLARINGOLOGISTA': 280,
    'PAPANICOLAU': 100,
    'PEDIATRA': 200,
    'PLASTICA': 350,
    'PNEUMOLOGISTA': 300,
    'PSICOLOGIA': 180,
    'PSIQUIATRIA': 350,
    'RADIOLOGIA': 150,
    'RESSONANCIA MAGNETICA': 900,
    'REUMATOLOGISTA': 300,
    'TESTE ERGOMETRICO': 250,
    'TOMOGRAFIA COMPUTADORIZADA': 600,
    'ULTRASSONOGRAFIA': 200,
    'UROLOGISTA': 300,
    'VASCULAR': 300
}

def definir_preco(esp):
    
    esp_formatada = str(esp).strip().upper()
    return tabela_precos.get(esp_formatada, 150)

print("Aplicando tabela de preços...")
df_real['Valor_Consulta'] = df_real['especialidade'].apply(definir_preco)


df_real['Status'] = 'Compareceu'

print("Gerando simulação de No-Shows...")
df_noshow = df_real.sample(frac=0.20, random_state=42).copy()


df_noshow['Status'] = 'No-Show'
df_noshow['stamp_senha'] = np.nan           
df_noshow['nps_nota'] = np.nan              
df_noshow['nps_observacoes'] = np.nan       


df_completo = pd.concat([df_real, df_noshow])


pasta_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')
caminho_final = os.path.join(pasta_downloads, 'Base_Drivers_NoShow_Completa.xlsx')

df_completo.to_excel(caminho_final, index=False)

print("-" * 30)
print(f"SUCESSO! Base gerada com TODAS as especialidades precificadas.")
print(f"Arquivo salvo em: {caminho_final}")
print("-" * 30)