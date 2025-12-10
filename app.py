"""
Prometheus V7 - Main Entry Point for Streamlit Cloud
"""
import streamlit as st
import json
from pathlib import Path
from datetime import datetime

# Page Config
st.set_page_config(
    page_title="Prometheus V7 - Dota 2 Analytics",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paths
DATABASE_PATH = Path(__file__).parent / "Database" / "Json"

def load_json(filepath):
    """Load JSON file safely."""
    try:
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        st.error(f"Error loading {filepath}: {e}")
    return {}

def load_dreamleague():
    """Load DreamLeague S26 data."""
    return load_json(DATABASE_PATH / "leagues" / "dreamleague_s26.json")

def load_events():
    """Load upcoming events."""
    data = load_json(DATABASE_PATH / "events" / "upcoming.json")
    return data.get("events", [])

def load_bets():
    """Load user bets."""
    data = load_json(DATABASE_PATH / "bets" / "user_bets.json")
    return data if data else {"bankroll": 1000, "bets": []}

def main():
    # Sidebar
    st.sidebar.title("🔥 Prometheus V7")
    st.sidebar.caption("Dota 2 Betting Analytics")
    
    page = st.sidebar.radio(
        "Navegação",
        ["🏠 Dashboard", "🏆 DreamLeague S26", "📅 Eventos", "💰 Apostas"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.caption(f"📅 {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    
    # Main Content
    if page == "🏠 Dashboard":
        render_dashboard()
    elif page == "🏆 DreamLeague S26":
        render_dreamleague()
    elif page == "📅 Eventos":
        render_events()
    elif page == "💰 Apostas":
        render_bets()

def render_dashboard():
    """Render main dashboard."""
    st.title("🔥 Prometheus V7")
    st.subheader("Dota 2 Analytics & Betting Platform")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    bets = load_bets()
    events = load_events()
    dl = load_dreamleague()
    
    with col1:
        st.metric("💵 Banca", f"R$ {bets.get('bankroll', 1000):.2f}")
    with col2:
        st.metric("📅 Eventos", len(events))
    with col3:
        teams = dl.get("teams", [])
        st.metric("🏆 Times DL S26", len(teams))
    with col4:
        st.metric("📊 Ligas", "40+")
    
    st.markdown("---")
    
    # Quick Links
    st.subheader("🚀 Acesso Rápido")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🏆 **DreamLeague S26**\n\nTorneio Tier 1 com os melhores times do mundo.")
        
    with col2:
        st.info("📅 **Próximos Eventos**\n\nCalendário completo de partidas.")
        
    with col3:
        st.info("💰 **Gestão de Apostas**\n\nRegistre e acompanhe suas apostas.")

def render_dreamleague():
    """Render DreamLeague S26 page."""
    st.title("🏆 DreamLeague Season 26")
    
    data = load_dreamleague()
    
    if not data:
        st.error("❌ Dados não carregados")
        return
    
    tournament = data.get("tournament", {})
    teams = data.get("teams", [])
    schedule = data.get("schedule", [])
    
    # Tournament Info
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💰 Prize Pool", tournament.get("prize_pool", "TBD"))
    with col2:
        st.metric("📅 Início", tournament.get("start_date", "TBD"))
    with col3:
        st.metric("🎮 Times", len(teams))
    with col4:
        st.metric("📺 Stream", "Twitch")
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2 = st.tabs(["📅 Partidas", "👥 Times"])
    
    with tab1:
        st.subheader("📅 Calendário de Partidas")
        
        for match in schedule:
            with st.container():
                col1, col2, col3 = st.columns([2, 3, 2])
                
                with col1:
                    st.caption(f"📅 {match.get('date')}")
                    st.write(f"🕐 **{match.get('time')}**")
                
                with col2:
                    team_a = match.get("team_a", "TBD")
                    team_b = match.get("team_b", "TBD")
                    st.write(f"**{team_a}** vs **{team_b}**")
                    st.caption(match.get("phase", ""))
                
                with col3:
                    odds = match.get("odds", {})
                    pred = match.get("prediction", {})
                    st.write(f"Odds: {odds.get('team_a', '-')} / {odds.get('team_b', '-')}")
                    st.caption(f"🤖 {pred.get('winner', 'N/A')} ({pred.get('confidence', 0)}%)")
                
                st.markdown("---")
    
    with tab2:
        st.subheader("👥 Times Participantes")
        
        for team in teams:
            tier_emoji = {"S": "🟣", "A": "🔵", "B": "🟢"}.get(team.get("tier"), "⚪")
            
            with st.expander(f"{tier_emoji} **{team.get('name')}** ({team.get('tag')})"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("🌍 Região", team.get("region", "N/A"))
                    st.metric("🏆 Ranking", f"#{team.get('ranking', 'N/A')}")
                
                with col2:
                    st.metric("📈 Win Rate", f"{team.get('win_rate', 0)}%")
                    form = team.get("recent_form", [])
                    form_str = " ".join(["✅" if f == "W" else "❌" for f in form])
                    st.write(f"📊 Forma: {form_str}")

def render_events():
    """Render events page."""
    st.title("📅 Próximos Eventos")
    
    events = load_events()
    
    if not events:
        st.info("Nenhum evento carregado.")
        return
    
    for event in events[:10]:
        with st.container():
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col1:
                st.caption(event.get("date", "TBD"))
                st.write(f"🕐 {event.get('time', 'TBD')}")
            
            with col2:
                st.write(f"**{event.get('team_a', 'TBD')}** vs **{event.get('team_b', 'TBD')}**")
                st.caption(event.get("league", "")[:50])
            
            with col3:
                st.write(f"📋 {event.get('format', 'Bo3')}")
            
            st.markdown("---")

def render_bets():
    """Render bets management page."""
    st.title("💰 Gestão de Apostas")
    
    bets_data = load_bets()
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("💵 Banca", f"R$ {bets_data.get('bankroll', 1000):.2f}")
    with col2:
        st.metric("📊 Apostas", len(bets_data.get("bets", [])))
    with col3:
        st.metric("📈 ROI", "N/A")
    
    st.markdown("---")
    
    # New Bet Form
    st.subheader("📝 Nova Aposta")
    
    with st.form("new_bet"):
        col1, col2 = st.columns(2)
        
        with col1:
            match = st.text_input("Partida", placeholder="Time A vs Time B")
            selection = st.text_input("Seleção", placeholder="Time A")
        
        with col2:
            odds = st.number_input("Odds", min_value=1.01, value=1.50, step=0.01)
            stake = st.number_input("Valor (R$)", min_value=10.0, value=50.0, step=10.0)
        
        potential = stake * odds
        st.info(f"💵 Retorno Potencial: **R$ {potential:.2f}**")
        
        submitted = st.form_submit_button("✅ Registrar Aposta")
        
        if submitted:
            st.success(f"✅ Aposta registrada: {selection} @ {odds}")

if __name__ == "__main__":
    main()
