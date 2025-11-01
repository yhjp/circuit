import streamlit as st

# -------------------------------
# 1️⃣ 회로 계산 함수
# -------------------------------

def series_resistance(resistors):
    return sum(resistors)

def parallel_resistance(resistors):
    if any(r == 0 for r in resistors):
        return 0
    return 1 / sum(1/r for r in resistors)

def led_resistor_calculator(v_supply, v_led, i_led_mA):
    """
    LED 전류 계산: R = (V_supply - V_led) / I_led
    i_led_mA: LED 전류 입력(mA)
    """
    i_led = i_led_mA / 1000  # mA → A
    if i_led == 0:
        return None
    return round((v_supply - v_led) / i_led, 2)

# -------------------------------
# 2️⃣ Streamlit UI
# -------------------------------
st.set_page_config(page_title="전자부품 계산기 💡", layout="centered")

st.title("💡 전자부품 계산기 & 회로 설계 도우미")
st.write("저항 계산, LED 전류 계산 등을 웹에서 바로 해보세요!")

# ----- 직렬/병렬 저항 계산 -----
st.subheader("1️⃣ 저항 계산기")

resistor_values = st.text_input(
    "저항값 입력(Ω, 콤마로 구분, 예: 100,220,330):"
)

resistors = []
if resistor_values:
    try:
        resistors = [float(r.strip()) for r in resistor_values.split(",")]
    except:
        st.error("저항값 입력이 잘못되었습니다. 숫자로 입력해주세요.")

if resistors:
    series_r = series_resistance(resistors)
    parallel_r = parallel_resistance(resistors)
    st.write(f"➡ 직렬 연결 총 저항: {series_r} Ω")
    st.write(f"➡ 병렬 연결 총 저항: {round(parallel_r,2)} Ω")

# ----- LED 저항 계산 -----
st.subheader("2️⃣ LED 저항 계산기")

v_supply = st.number_input("공급 전압(V)", value=5.0)
v_led = st.number_input("LED 전압 강하(V)", value=2.0)
i_led = st.number_input("LED 전류(mA)", value=20.0)

if st.button("계산"):
    r_led = led_resistor_calculator(v_supply, v_led, i_led)
    if r_led is not None:
        st.success(f"➡ LED 저항값: {r_led} Ω")
    else:
        st.error("전류값을 0이 아닌 값으로 입력해주세요.")

# -------------------------------
# 3️⃣ 추가 안내
# -------------------------------
st.markdown("---")
st.write("이 앱을 활용해 간단한 회로 설계와 계산을 연습할 수 있습니다.")

st.write("생기부에 기록할 때는 ‘전자회로 계산 및 설계 웹앱 제작 경험’으로 작성 가능")
