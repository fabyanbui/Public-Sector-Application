import streamlit as st
import pandas as pd
import google.generativeai as genai
import ast
import time

template = \
"""TÔI SẼ ĐƯA CHO BẠN MỘT TRƯỜNG THÔNG TIN LÀ {col_name} CỦA MỘT THỦ TỤC HÀNH CHÍNH. BẠN KHÔNG CẦN PHẢI SUY LUẬN GÌ CẢ.
KHÔNG ĐƯỢC THAY ĐỔI BẤT KỲ NỘI DUNG GÌ. CHỈ KIỂM TRA LỖI CHÍNH TẢ VÀ SỬA LẠI CHO ĐÚNG:

{information}
"""

long = 200
short = 100

def main(api):
    genai.configure(api_key=api)
    gem = genai.GenerativeModel('gemini-2.0-flash')

    file_path = "annotated_data/second_tthc.csv"
    revert_path = "preprocessed_data/second_tthc.csv"

    def load_data(path):
        tmp_df = pd.read_csv(path, dtype={'maThuTuc': str})

        return tmp_df
        
    df = load_data(file_path)
    revert_df = load_data(revert_path)

    index = st.number_input(
        " Chọn dòng để chỉnh sửa:",
        min_value=int(df.index.min()),
        max_value=int(df.index.max()),
        value=int(df.index.min()),
        step=1,
        format="%d",
        key=f'number_input_{file_path}'
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        col11, col12 = st.columns([1, 1])
        with col11:
            st.markdown(f"** Link:** [Truy cập]({df.loc[index]['link']})")
        with col12:
            st.markdown(f"**🆔 Mã thủ tục:** {df.loc[index]['maThuTuc']}")

    with col2:
        col21, col22 = st.columns([1, 1])
        with col21:
            st.markdown(f"**Checked:** {'Yes' if df.loc[index]['checked'] else 'No'}")
        with col22:
            st.markdown(f"** Last updated:** {str(df.loc[index]['lastUpdated'])}")

    cols = df.drop(columns=['link', 'maThuTuc', 'checked', 'lastUpdated']).columns

    col_s1, col_s2, col_s3, col_s4 = st.columns([1, 1, 1, 1])

    col1, col2 = st.columns([1, 1])

    with col1:
        for col in cols:
            st.text_area(col, df[col][index], long, key=f'{col}_{index}_{file_path}')

    def on_b1_clicked():
        df.loc[index] = revert_df.loc[index]

        for col in cols:
            st.session_state[f'{col}_{index}_{file_path}'] = df[col][index]
        
        # df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.to_csv(file_path, index=False)

    def on_b2_clicked():
        df.at[index, 'checked'] = False

        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.to_csv(file_path, index=False)

    def on_b3_clicked():
        df.at[index, 'checked'] = True

        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.to_csv(file_path, index=False)

    def on_b4_clicked():
        df.at[index, 'checked'] = True

        for col in cols:
            df.at[index, col] = st.session_state[f'{col}_{index}_{file_path}']

        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.to_csv(file_path, index=False)

    with col_s1:
        b1 = st.button(' Revert', help='Back to initial data and save to CSV', on_click=on_b1_clicked, key=f'b1_{index}_{file_path}')

    with col_s2:
        b2 = st.button(' Unchecked', help='Only uncheck and save to CSV', on_click=on_b2_clicked, key=f'b2_{index}_{file_path}')

    with col_s3:
        b3 = st.button(' Checked', help='Only check and save to CSV', on_click=on_b3_clicked, key=f'b3_{index}_{file_path}')

    with col_s4:
        b4 = st.button(' Save', help='Update values in textbox and save to CSV', on_click=on_b4_clicked, key=f'b4_{index}_{file_path}')

    with col2:
        for col in cols:
            st.text_area(f'Gemini đề xuất cho {col}', "", long, disabled=True, key=f'suggested_{col}_{index}_{file_path}')

    def on_btn_clicked():
        for col in cols:
            if st.session_state[f'suggested_{col}_{index}_{file_path}'] != "":
                if "429 You exceeded your current quota" not in st.session_state[f'suggested_{col}_{index}_{file_path}']:
                    continue
                if 'Không có thông tin' in st.session_state[f'{col}_{index}_{file_path}']:
                    continue
                if col in ['maThuTuc', 'soQuyetDinh', 'capThucHien', 'loaiThuTuc', 'linhVuc']:
                    continue
                if len(st.session_state[f'{col}_{index}_{file_path}']) < 10:
                    continue
            prompt = template.format(col_name=col, information=df[col][index])
            try:
                output = gem.generate_content(prompt).text.strip()
            except Exception as e:
                output = str(e)
            st.session_state[f'suggested_{col}_{index}_{file_path}'] = output

    _, col_btn = st.columns([1, 1])
    with col_btn:
        btn = st.button(' Generate', on_click=on_btn_clicked, key=f'btn_{index}_{file_path}')

    st.markdown("---")
    st.write(df.loc[index])
    st.dataframe(df)
