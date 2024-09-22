import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Streamlit 앱 타이틀 설정
st.title("Mermaid Diagram Generator")

# 탭 생성
tabs = st.tabs(["Custom Diagram", "Sample 1", "Sample 2"])

with tabs[0]:
    st.header("Custom Diagram")

    # 노드와 화살표 방향 입력 받기
    col1, col2 = st.columns([1, 1])
    with col1:
        nodes = st.text_area("Enter nodes (comma separated)", "A, B, C")
    with col2:
        direction_type = st.selectbox("Select direction type", ["LR (Left to Right)", "TD (Top to Down)"], index=0)

    directions = st.text_area("Mermaid code : Enter directions (one per line)", "A --> B\nB --> C", height=200)

    direction_code = "LR" if "LR" in direction_type else "TD"

    # 노드 리스트와 방향 리스트 생성
    node_list = nodes.split(',')
    direction_list = directions.split('\n')

    # Mermaid 코드 생성
    mermaid_code = f"graph {direction_code}\n"
    for direction in direction_list:
        mermaid_code += f"    {direction.strip()}\n"

    # Mermaid 코드 출력
    st.subheader("Mermaid Code")
    st.code(mermaid_code, language='markdown')

    # Mermaid 다이어그램을 HTML로 삽입
    st.header("Generated Mermaid Diagram")
    components.html(f"""
        <div class="mermaid">
        {mermaid_code}
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
    """, height=500)


with tabs[1]:
    st.header("Sample 1")

    sample_code_1 = """
flowchart LR

classDef yellow fill:yellow, stroke:black, stroke-width:2px, color:black

node(홍길동)
n2((홍당무)):::yellow
node-->|즐겨먹는 간식|n2

style node stroke:red,color:white,fill:blue,stroke-width:4px
linkStyle 0 stroke:red
    """

    # Mermaid 코드 출력
    st.subheader("Mermaid Code")
    st.code(sample_code_1, language='markdown')

with tabs[2]:
    st.header("Sample 2")

    sample_code_2 = """
flowchart TD
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    B -->|No| D[Not OK]
    C --> E[End]
    D --> E
    """

    # Mermaid 코드 출력
    st.subheader("Mermaid Code")
    st.code(sample_code_2, language='markdown')
