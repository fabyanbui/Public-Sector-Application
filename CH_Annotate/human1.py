import streamlit as st
import pandas as pd
import ast

pattern = []

pattern.append("Hiểu sai ngữ cảnh và mục đích của câu hỏi đó")
pattern.append("Mâu thuẫn giữa câu trả lời và kiến thức liên quan")
pattern.append("Quá chung chung hoặc quá chi tiết")
pattern.append("Câu trả lời không thể suy ra từ kiến thức liên quan (suy luận sai)")

def main():
    file_path = 'annotated_data/human1.csv'

    df = pd.read_csv(file_path)

    for col in ["phanLoai", "TTHCLienQuan", "cauHoiLienQuan"]:
        df[col] = df[col].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else [])

    index = st.number_input(
        " Chọn dòng để chỉnh sửa:",
        min_value=int(df.index.min()),
        max_value=int(df.index.max()),
        value=int(df.index.min()),
        step=1,
        format="%d",
        key=f'number_input_{file_path}'
    )

    st.write(f"**Câu hỏi:** {df.iloc[index]['cauHoi']}")
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.write(f"**Pattern:** {pattern[df.iloc[index]['pattern']]}")

    with col2:
        col2_1, col2_2 = st.columns([1, 1])
        with col2_1:
            st.write(f"**Checked:** {df.iloc[index]['checked']}")
        with col2_2:
            st.write(f"**Hallucinated:** {df.iloc[index]['hallucinated']}")

    def on_b1():
        df.at[index, 'checked'] = False
        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.at[index, 'hallucinated'] = False
        df.at[index, 'rightPattern'] = False
        df.to_csv(file_path, index=False)

    def on_b2():
        df.at[index, 'checked'] = True
        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.at[index, 'hallucinated'] = False
        df.at[index, 'rightPattern'] = False
        df.to_csv(file_path, index=False)

    def on_b3():
        df.at[index, 'checked'] = True
        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.at[index, 'hallucinated'] = True
        df.at[index, 'rightPattern'] = False
        df.to_csv(file_path, index=False)

    def on_b4():
        df.at[index, 'checked'] = True
        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.at[index, 'hallucinated'] = True
        df.at[index, 'rightPattern'] = True
        df.to_csv(file_path, index=False)

    b1, b2, b3, b4 = st.columns([1, 1, 1, 1])
    with b1:
        st.button('Unchecked', on_click=on_b1, key=f'{index}_{file_path}_b1')
    with b2:
        st.button('False hallucination', on_click=on_b2, key=f'{index}_{file_path}_b2')
    with b3:
        st.button('Only false pattern', on_click=on_b3, key=f'{index}_{file_path}_b3')
    with b4:
        st.button('True hallucination', on_click=on_b4, key=f'{index}_{file_path}_b4')

    col1, col2 = st.columns([1, 1])

    with col1:
        # st.header('Câu trả lời đúng')
        st.text_area("**Câu trả lời đúng:**", value=df.loc[index]['cauTraLoi'], height=300, key=f'{index}_{file_path}_right')
        # st.markdown(df.loc[index]['cauTraLoi'])

    with col2:
        # st.header('Câu trả lời ảo giác')
        st.text_area("**Câu trả lời ảo giác:**", value=df.loc[index]['cauTraLoiAoGiac'], height=300, key=f'{index}_{file_path}_hallucinated')
        # st.markdown(df.loc[index]['cauTraLoiAoGiac'])

    col1, col2 = st.columns([1, 1])

    with col1:
        with st.expander(" TTHC liên quan"):
            if df.loc[index]['TTHCLienQuan']:
                for link in df.loc[index]['TTHCLienQuan']:
                    st.markdown(f"- {link}")
            else:
                st.write("Không có.")

    with col2:
        with st.expander(" Câu hỏi liên quan"):
            if df.loc[index]['cauHoiLienQuan']:
                for link in df.loc[index]['cauHoiLienQuan']:
                    st.markdown(f"- {link}")
            else:
                st.write("Không có.")

    st.dataframe(df)