# Escape Room Escolar

Jogo educativo 2D desenvolvido em grupo como projeto escolar.

## Sobre o projeto

O **Escape Room Escolar** é um jogo 2D desenvolvido em Python e Pygame.

O jogador está preso dentro de uma escola e precisa explorar o ambiente, encontrar pistas, resolver perguntas educativas e liberar o caminho até a saída.

O objetivo principal é criar uma experiência simples de Escape Room utilizando conceitos de programação e desenvolvimento de jogos.

## Objetivo do MVP

O MVP deve permitir que o jogador:

1. Inicie o jogo.
2. Explore a escola.
3. Encontre pistas.
4. Interaja com objetos usando `E`.
5. Responda perguntas educativas.
6. Libere áreas.
7. Encontre a saída.
8. Veja a tela de vitória.

## Tecnologias

* Python 3
* Pygame
* Git/GitHub

## Controles

| Tecla | Função                         |
| ----- | ------------------------------ |
| W / ↑ | Mover para cima                |
| S / ↓ | Mover para baixo               |
| A / ← | Mover para esquerda            |
| D / → | Mover para direita             |
| E     | Interagir                      |
| ESC   | Voltar/pausar, se implementado |

## Estrutura

```text
escape-room-school/
│
├── main.py
├── player.py
├── settings.py
├── questions.py
│
├── assets/
│   ├── images/
│   ├── sounds/
│   └── fonts/
│
└── README.md
```

A estrutura pode ser simplificada ou modificada durante o desenvolvimento caso isso facilite a implementação.

## Desenvolvimento

O projeto será desenvolvido de forma incremental.

Prioridade:

```text
FUNCIONAR
   ↓
JOGABILIDADE
   ↓
CONTEÚDO
   ↓
VISUAL
   ↓
POLIMENTO
```

Recursos que não forem necessários para o MVP podem ser removidos ou deixados para uma versão futura.

## Funcionalidades planejadas

### Básico

* [x] Janela do jogo
* [x] Jogador
* [x] Movimento
* [x] Colisão básica
* [ ] Mapa completo
* [ ] Salas
* [ ] Portas
* [ ] Interação
* [ ] Pistas
* [ ] Perguntas
* [ ] Progressão
* [ ] Saída
* [ ] Tela de vitória

### Futuro, se houver tempo

* [ ] Sprites
* [ ] Sons
* [ ] Música
* [ ] Animações
* [ ] Melhorias visuais
* [ ] Mais perguntas
* [ ] Mais áreas da escola

## Execução

Clone ou abra o projeto e instale o Pygame:

```bash
python -m pip install pygame
```

Execute:

```bash
python main.py
```

## Organização do grupo

O projeto é desenvolvido em grupo. As tarefas devem ser divididas entre os integrantes de acordo com o planejamento da equipe.

Alterações importantes devem ser testadas antes de serem integradas ao projeto principal.

## Princípios do projeto

* Manter o código simples.
* Evitar funcionalidades desnecessárias.
* Priorizar o funcionamento do jogo.
* Testar cada funcionalidade antes de adicionar outra.
* Evitar alterações grandes sem necessidade.
* Utilizar IA como ferramenta de auxílio, mantendo o código compreensível para a equipe.

## Status

**Em desenvolvimento — MVP**

O projeto está sendo construído de forma incremental, começando pelas mecânicas fundamentais e adicionando as funcionalidades necessárias para completar o Escape Room.
