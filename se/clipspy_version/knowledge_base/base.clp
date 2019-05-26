
;; Define o modelo de torre
(deftemplate torre
    (slot operacao (type SYMBOL))
)

;; Define os dados inputados
(deftemplate data
    (slot ph (type FLOAT))
    (slot vazao_produto (type FLOAT))
    (slot vazao_agua_lavagem (type FLOAT))
    (slot injecao_neutralizante (type FLOAT))
)

;; Se não for fornecido o fato com os dados, pedir para o usuário inputar
(defrule read_vazao_produto
    (initial-fact)
    (not (exists (data)))
=>
    (printout t "Digite a Vazão Produto: ")
    (assert (data (vazao_produto (read))))
)

;; Pergunta o PH se necessário
(defrule read_ph
    ?data <- (data (ph ?var))
    (test (= 0 ?var))
=>
    (printout t "Digite o ph: ")
    (modify ?data (ph (read)))
)

;; Pergunta a Vazão de Água lavagem se necessário
(defrule read_vazao_agua_lavagem
    ?data <- (data (vazao_agua_lavagem ?var))
    (test (= 0.0 ?var))
=>
    (printout t "Digite a vazão de água lavagem: ")
    (modify ?data (vazao_agua_lavagem (read)))
)

;; Pergunta a Injeção neutralizante se necessário
(defrule read_injecao_neutralizante
    ?data <- (data (injecao_neutralizante ?var))
    (test (= 0.0 ?var))
=>
    (printout t "Digite a Injeção de neutralidade: ")
    (modify ?data (injecao_neutralizante (read)))
)


;; Regra para definir se a torre está em operação
(defrule em_operacao
    (data (vazao_produto ?vazao_produto))
    (test(> ?vazao_produto 0))
=>
    (assert (torre (operacao operando)))
)

;; SE torre operando E PH = 5.9
;; Então sob-controle
(defrule normal_state
    (torre (operacao operando))
    (data (ph ?ph))
    (test (= ?ph 5.9))
=>
    (printout t "Corrosão sob controle na torre" crlf)    
)

;; SE PH = 5.0 E VAZAO Água Lavagem < 130+10% E VAZAO Água Lavagem < 115 ENTÃO
;; Risco Elevado de corrosão e Ajustar Vazão água lavagem para > 130 - 10%
(defrule increase_vazao_lavagem
    (torre (operacao operando))
    (data (ph ?ph) (vazao_agua_lavagem ?vazao_agua_lavagem))
    (test (= ?ph 5.0))
    (test (< ?vazao_agua_lavagem (* 130 1.1)))
    (test (< ?vazao_agua_lavagem 115))
=>
    (printout t "Risco elevado de corrosão na torre" crlf)
    (printout t (str-cat "Ajustar a vazão de água de lavagem para >" (* 130 0.9)) crlf)
)

;; SE PH = 5.0 E Vazão água lavagem sendo 130 +/- 10% ENTÃO
;; Risco Elevado de corrosão e Aumentar a injeção de neutralidade em 10%
(defrule increase_neutralizante
    (torre (operacao operando))
    (data (ph ?ph) (vazao_agua_lavagem ?vazao_agua_lavagem))
    (test (= ?ph 5.0))
    (test (< ?vazao_agua_lavagem (* 130 1.1)))
    (test (> ?vazao_agua_lavagem (* 130 0.9)))
=>
    (printout t "Risco elevado de corrosão na torre" crlf)
    (printout t "Aumentar a injeção de neutralizante em 10%" crlf)
)
