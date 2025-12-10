# 🔥 PROMETHEUS V7

> **Plataforma de Análise e Previsão para Dota 2 - European Pro League (EPL)**

## 📋 Sobre o Projeto

Prometheus é uma plataforma avançada de análise e previsão para **Dota 2**, especializada na **European Pro League (EPL)**. O sistema combina inteligência artificial, análise de dados históricos e gestão de apostas.

### Principais Funcionalidades

- 🎮 **Análise de Partidas**: 7.247+ partidas profissionais analisadas
- 🤖 **Sistema GEM**: IA especializada em previsões de apostas
- 📊 **Meta de Heróis**: 126 heróis com tier list S/A/B/C/D
- 👥 **Perfis de Times**: 40 temporadas de dados históricos
- 💰 **Gestão de Apostas**: Tracking com Kelly Criterion
- 🔧 **Arquimedes**: Orquestrador de múltiplos agentes IA

## 📁 Estrutura do Projeto

```
Sistema Prometheus/
├── v7.0.1/                    # Versão atual
│   ├── Agentes/Arquimedes/    # Orquestrador IA
│   ├── Database/              # Base de dados + Documentação
│   ├── Images/                # Imagens de heróis
│   └── Jupiter notebook/      # Notebooks ML
├── DOCUMENTATION.md           # Documentação completa
├── INVENTORY.md               # Inventário de arquivos
├── SETUP_GUIDE.md             # Guia de instalação
├── MIGRATION_PLAN.md          # Plano de migração
└── README.md                  # Este arquivo
```

## 🚀 Quick Start

```powershell
# 1. Clone o projeto
git clone <repository-url>

# 2. Configure credenciais
copy CREDENTIALS_TEMPLATE.env .env
# Edite .env com suas API keys

# 3. Para usar o Arquimedes
cd v7.0.1/Agentes/Arquimedes/V1.0
pnpm install
pnpm dev
```

## 📖 Documentação

| Arquivo | Conteúdo |
|---------|----------|
| `DOCUMENTATION.md` | Documentação técnica completa |
| `INVENTORY.md` | Inventário e categorização de arquivos |
| `SETUP_GUIDE.md` | Guia de instalação e configuração |
| `MIGRATION_PLAN.md` | Plano de migração para Drive |

## 🔑 APIs Necessárias

| API | Uso |
|-----|-----|
| Steam Web API | Dados ao vivo |
| OpenDota API | Dados históricos |
| OpenRouter | LLMs (Claude/GPT) |

## 📊 Estatísticas

| Métrica | Valor |
|---------|-------|
| Heróis | 126 |
| Partidas EPL | 7.247+ |
| Times | 37+ |
| Jogadores | 812 |
| Ligas | 20+ |

## 📅 Versões

| Versão | Status |
|--------|--------|
| V7.0.1 | ✅ Atual |
| V6.x | 📦 Arquivado |
| V5.x | 📦 Arquivado |

---

**Última atualização**: 09/12/2025
