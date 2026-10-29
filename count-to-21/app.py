import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="CountTo21",
    page_icon="🎯",
    layout="centered"
)

# ==========================================
# 2. GAME TITLE AND RULES
# ==========================================
st.title("🎯 CountTo21")
st.write("Can you beat the robot?")

with st.expander("📖 Game Rules", expanded=True):
    st.write("""
    1. The player who says 21 loses!
    2. Each player can add 1, 2, or 3 numbers.
    3. The player starts first.
    """)

st.divider()

# ==========================================
# 3. INITIALISE SESSION STATE
# ==========================================
if "started" not in st.session_state:
    st.session_state.started = False

if "current" not in st.session_state:
    st.session_state.current = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "result" not in st.session_state:
    st.session_state.result = ""

# ==========================================
# 4. START AND RESTART BUTTONS
# ==========================================
if not st.session_state.started:

    if st.button("🚀 Start Game", use_container_width=True):
        st.session_state.started = True
        st.session_state.current = 0
        st.session_state.history = []
        st.session_state.game_over = False
        st.session_state.result = ""
        st.rerun()

elif st.session_state.game_over:

    if st.session_state.result == "player":
        st.error("🤖 You said 21! The robot wins!")

    elif st.session_state.result == "robot":
        st.success("🎉 The robot said 21! You win!")

    if st.button("🔄 Play Again", use_container_width=True):
        st.session_state.current = 0
        st.session_state.history = []
        st.session_state.game_over = False
        st.session_state.result = ""
        st.rerun()

# ==========================================
# 5. MAIN GAME
# ==========================================
if st.session_state.started and not st.session_state.game_over:

    st.subheader("🎮 Your Turn")

    st.metric(
        label="Current Number",
        value=st.session_state.current
    )

    player = st.selectbox(
        "How many numbers would you like to add?",
        options=[1, 2, 3]
    )

    if st.button("Submit Move", use_container_width=True):

        # PLAYER'S TURN
        for _ in range(player):

            st.session_state.current += 1

            st.session_state.history.append(
                ("You", st.session_state.current)
            )

            if st.session_state.current == 21:
                st.session_state.game_over = True
                st.session_state.result = "player"
                break

        # ROBOT'S TURN
        if not st.session_state.game_over:

            win = [4, 8, 12, 16, 20]

            target = next(
                (
                    number
                    for number in win
                    if number > st.session_state.current
                ),
                None
            )

            if target is not None:

                while st.session_state.current < target:

                    st.session_state.current += 1

                    st.session_state.history.append(
                        ("Robot", st.session_state.current)
                    )

        # REFRESH THE INTERFACE
        st.rerun()

# ==========================================
# 6. GAME HISTORY
# ==========================================
st.divider()
st.subheader("📜 Game History")

if not st.session_state.history:

    st.caption("Your moves will appear here once the game begins.")

else:

    for player_name, number in st.session_state.history:

        if player_name == "You":
            st.write(f"🧑 **You:** {number}")

        else:
            st.write(f"🤖 **Robot:** {number}")
