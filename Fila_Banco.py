import random

class NoCliente:
    def __init__(self, senha):
        self.senha = senha
        self.prox = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.final = None
    
    def vazia(self):
        return self.inicio is None
    
    def enqueue(self, senha):
        novo = NoCliente(senha)
        if self.vazia():
            self.inicio = self.final = novo
        else:
            self.final.prox = novo
            self.final = novo
    
    def dequeue(self):
        if self.vazia():
            raise IndexError("Dequeue em fila vazia")
        no = self.inicio
        if self.inicio == self.final:
            self.inicio = self.final = None
        else:
            self.inicio = self.inicio.prox
        senha = no.senha
        no.prox = no.senha = None
        return senha
    
    def para_lista(self):
        elementos = []
        temp = self.inicio
        while temp != None:
            elementos.append(temp.senha)
            temp = temp.prox
        return elementos
    
def simular_banco(tempo_total_simulacao=20, prob_chegada=0.5, tempo_atendimento=3):
    fila_normal = Fila()
    fila_preferencial = Fila()
    
    count_normal = 0
    count_preferencial = 0
    
    cliente_em_atendimento = None
    tempo_restante_atendimento = 0
    normais_seguidos = 0
    
    print(f"Chance de chegada de cliente: {int(prob_chegada * 100)}% a cada segundo")
    print(f"Atendimento fixo: {tempo_atendimento}s por cliente")
    print(f"{'Tempo (s)':<10} | {'Evento':<55} | {'Fila Normal':<18} | {'Fila Pref. (P)':<15} | {'Atendimento':<10}")
    print("-" * 125)

    for t in range(tempo_total_simulacao + 1):
        eventos = []
        
        # 1. Verifica término de atendimento
        if cliente_em_atendimento is not None:
            tempo_restante_atendimento -= 1
            if tempo_restante_atendimento == 0:
                eventos.append(f"Fim do atendimento {cliente_em_atendimento}")
                cliente_em_atendimento = None
        
        # 2. Gera Chegada aleatória de novo cliente
        if random.random() < prob_chegada:
            if random.choice(['N', 'P']) == 'N':
                count_normal += 1
                senha = f"N{count_normal}"
                fila_normal.enqueue(senha)
                eventos.append(f"Chega {senha}")
            else:
                count_preferencial += 1
                senha = f"P{count_preferencial}"
                fila_preferencial.enqueue(senha)
                eventos.append(f"Chega {senha}")
        
        # 3. Seleciona novo cliente caso o guichê esteja livre
        if cliente_em_atendimento is None:
            # Regra: 2 Normais -> 1 Preferencial
            escolher_preferencial = ((normais_seguidos >= 2 and not fila_preferencial.vazia()) 
                                     or 
                                     (fila_normal.vazia() and not fila_preferencial.vazia()))
            if escolher_preferencial:
                cliente_em_atendimento = fila_preferencial.dequeue()
                if cliente_em_atendimento:
                    tempo_restante_atendimento = tempo_atendimento
                    normais_seguidos = 0
                    eventos.append(f"Inicia {cliente_em_atendimento} ({tempo_atendimento})s")
            elif not fila_normal.vazia():
                cliente_em_atendimento = fila_normal.dequeue()
                if cliente_em_atendimento:
                    tempo_restante_atendimento = tempo_atendimento
                    normais_seguidos += 1
                    eventos.append(f"Inicia {cliente_em_atendimento} ({tempo_atendimento})s")
        # Formatação para exibição
        str_evento = ", ".join(eventos) if eventos else ""
        
        if t == 0:
            str_evento = "Início do sistema"
        
        str_normais = str(fila_normal.para_lista())
        str_pref = str(fila_preferencial.para_lista())
        str_atend = cliente_em_atendimento if cliente_em_atendimento else ""
        
        print(f"{t:<10} | {str_evento:<55} | {str_normais:<18} | {str_pref:<15} | {str_atend:<10}")

# --- Testes ---
if __name__ == "__main__":
    random.seed(42)  # Semente fixa para simulação reproduzível
    print("=== TESTE Q4: FLUXO BANCÁRIO ===")
    print()
    simular_banco(tempo_total_simulacao=15, prob_chegada=0.5, tempo_atendimento=3)