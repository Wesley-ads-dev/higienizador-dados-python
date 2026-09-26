# SISTEMA DE HIGIENIZAÇÃO E SEGURANÇA DE DADOS)
# Autor: Wesley Santana
# Objetivo: Demonstrar tratamento de strings, sanitização e anti-fraude.
# ==============================================================================
def processar_cadastro():
    print("--- EMULADOR DE SISTEMA CORPORATIVO (BACKEND) ---")

    nome_usuario = input("Digite o nome completo do cliente: ").strip()
    nome_minusculo = nome_usuario.lower()
    
    
    if "teste" in nome_minusculo or "admin" in nome_minusculo:
        print("🚨 LOG DE SEGURANÇA: Cadastro rejeitado. Palavra proibida detectada.")
        return

    cpf_bruto = input("Digite o CPF do cliente (com pontos/traços): ")
    cpf_limpo = cpf_bruto.replace(".", "").replace("-", "").replace(" ", "")

    if len(cpf_limpo) != 11:
        print(f"❌ ERRO DE VALIDAÇÃO: CPF inválido! Esperado 11 dígitos, mas você informou {len(cpf_limpo)}.")
        return

    print("\n==================================================")
    print("📋 DADOS PROCESSADOS COM SUCESSO (PRONTOS PARA O BANCO):")
    print(f"👤 Cliente: {nome_usuario}")
    print(f"🗄️ CPF Sanitizado: {cpf_limpo}")
    print(f"🔢 Digitos do CPF: {len(cpf_limpo)} (Status: Válido)")
    print("==================================================")

if __name__ == "__main__":
    processar_cadastro()
