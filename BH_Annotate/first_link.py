import streamlit as st
import pandas as pd
import google.generativeai as genai
import ast

def main(api):
    genai.configure(api_key=api)
    gem = genai.GenerativeModel('gemini-2.0-flash')

    file_path = "annotated_data/first_link.csv"
    revert_path = "preprocessed_data/first_link.csv"

    def load_data(path):
        tmp_df = pd.read_csv(path, dtype={'lastUpdated': str})
        
        for col in ["phanLoai", "TTHCLienQuan", "cauHoiLienQuan"]:
            tmp_df[col] = tmp_df[col].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else [])
        return tmp_df

    df = load_data(file_path)
    revert_df = load_data(revert_path)

    index = st.number_input(
        "🔎 Chọn dòng để chỉnh sửa:",
        min_value=int(df.index.min()),
        max_value=int(df.index.max()),
        value=int(df.index.min()),
        step=1,
        format="%d"
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(f"**🔗 Link:** [{df.loc[index]['link']}]({df.loc[index]['link']})")

    with col2:
        col21, col22 = st.columns([1, 1])
        with col21:
            st.markdown(f"**✎ Checked:** {"✅" if df.loc[index]['checked'] else "❌"}")
        with col22:
            st.markdown(f"**📅 Last updated:** {str(df.loc[index]['lastUpdated'])}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**🏛️ Bộ/ngành:** {df.loc[index]['boNganh']}")

    with col2:
        phanloai_set = set(df.loc[index]['phanLoai'])
        phanloai_mapping = {
            "công dân": "👤 Công dân",
            "doanh nghiệp": "🏢 Doanh nghiệp",
            "tổ chức khác": "🏛️ Tổ chức khác"
        }
        phanloai_str = [phanloai_mapping.get(p.lower(), p) for p in phanloai_set]
        phanloai_str = " | ".join(phanloai_str) if phanloai_str else "🚫 Không phân loại"
        st.markdown(f"**📂 Phân loại:** {phanloai_str}")

    col1, col2 = st.columns([1, 1])

    with col1:
        with st.expander("📌 TTHC liên quan"):
            if df.loc[index]['TTHCLienQuan']:
                for link in df.loc[index]['TTHCLienQuan']:
                    st.markdown(f"- {link}")
            else:
                st.write("Không có.")

    with col2:
        with st.expander("❓ Câu hỏi liên quan"):
            if df.loc[index]['cauHoiLienQuan']:
                for link in df.loc[index]['cauHoiLienQuan']:
                    st.markdown(f"- {link}")
            else:
                st.write("Không có.")

    original_question = df.loc[index]['cauHoi']
    original_answer = df.loc[index]['cauTraLoi']

    question_prompt = \
f"""TÔI SẼ ĐƯA CHO BẠN MỘT CÂU HỎI. BẠN KHÔNG CẦN TRẢ LỜI GÌ CẢ.
KHÔNG ĐƯỢC CHỈNH SỬA BẤT KỲ NỘI DUNG GÌ. CHỈ KIỂM TRA LỖI CHÍNH TẢ VÀ SỬA LẠI CHO ĐÚNG:

{original_question}
"""
    answer_prompt = \
f"""TÔI SẼ ĐƯA CHO BẠN MỘT VĂN BẢN. BẠN KHÔNG CẦN SUY LUẬN GÌ CẢ.
KHÔNG ĐƯỢC CHỈNH SỬA BẤT KỲ NỘI DUNG GÌ. CHỈ KIỂM TRA LỖI CHÍNH TẢ VÀ SỬA LẠI CHO ĐÚNG:

{original_answer}
"""

    col_s1, col_s2, col_s3, col_s4 = st.columns([1, 1, 1, 1])

    col1, col2 = st.columns([1, 1])

    with col1:
        cauHoi = st.text_area("🟦 Câu hỏi gốc (có thể chỉnh sửa)", original_question, height=400, key=f'cauHoi_{index}_{file_path}')

    with col2:
        cauTraLoi = st.text_area("🟩 Câu trả lời gốc (có thể chỉnh sửa)", original_answer, height=400, key=f'cauTraLoi_{index}_{file_path}')

    def on_b1_clicked():
        # df.at[index, 'checked'] = False
        df.loc[index] = revert_df.loc[index]

        st.session_state[f'cauHoi_{index}_{file_path}'] = df.loc[index]['cauHoi']
        st.session_state[f'cauTraLoi_{index}_{file_path}'] = df.loc[index]['cauTraLoi']
        
        # df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.to_csv(file_path, index=False)

    def on_b2_clicked():
        df.at[index, 'checked'] = False
        # df.loc[index] = revert_df.loc[index]

        # st.session_state[f'cauHoi_{index}_{file_path}'] = df.loc[index]['cauHoi']
        # st.session_state[f'cauTraLoi_{index}_{file_path}'] = df.loc[index]['cauTraLoi']

        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.to_csv(file_path, index=False)

    def on_b3_clicked():
        df.at[index, 'checked'] = True
        # df.at[index, 'cauHoi'] = cauHoi
        # df.at[index, 'cauTraLoi'] = cauTraLoi

        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.to_csv(file_path, index=False)

    def on_b4_clicked():
        df.at[index, 'checked'] = True
        df.at[index, 'cauHoi'] = cauHoi
        df.at[index, 'cauTraLoi'] = cauTraLoi

        df.at[index, 'lastUpdated'] = str(pd.Timestamp.now())
        df.to_csv(file_path, index=False)

    with col_s1:
        b1 = st.button('🔄 Revert', help='Back to initial data and save to CSV', on_click=on_b1_clicked, key=f'b1_{index}_{file_path}')

    with col_s2:
        b2 = st.button('❌ Unchecked', help='Only uncheck and save to CSV', on_click=on_b2_clicked, key=f'b2_{index}_{file_path}')

    with col_s3:
        b3 = st.button('✅ Checked', help='Only check and save to CSV', on_click=on_b3_clicked, key=f'b3_{index}_{file_path}')

    with col_s4:
        b4 = st.button('💾 Save', help='Update values in textbox and save to CSV', on_click=on_b4_clicked, key=f'b4_{index}_{file_path}')

    st.markdown("---")
    st.write(df.loc[index])
    st.dataframe(df[['checked', 'lastUpdated', 'cauHoi', 'cauTraLoi', 'boNganh', 'phanLoai', 'link', 'TTHCLienQuan', 'cauHoiLienQuan']], use_container_width=True)

    with col1:
        if f"suggested_question_{index}_{file_path}" not in st.session_state:
            try:
                st.session_state[f"suggested_question_{index}_{file_path}"] = gem.generate_content(question_prompt).text.strip()
                st.text_area("🤖 Câu hỏi đề xuất từ Gemini", st.session_state[f"suggested_question_{index}_{file_path}"], 
                             height=400, disabled=True, key=f"suggested_question_{index}_{file_path}")
            except Exception as e:
                st.text_area("🤖 Câu hỏi đề xuất từ Gemini", str(e), 
                             height=400, disabled=True, key=f"suggested_question_{index}_{file_path}")
        else:
            st.text_area("🤖 Câu hỏi đề xuất từ Gemini", st.session_state[f"suggested_question_{index}_{file_path}"], 
                         height=400, disabled=True, key=f"suggested_question_{index}_{file_path}")
        
    with col2:
        if f"suggested_answer_{index}_{file_path}" not in st.session_state:
            try:
                st.session_state[f"suggested_answer_{index}_{file_path}"] = gem.generate_content(answer_prompt).text.strip()
                st.text_area("🤖 Câu trả lời đề xuất từ Gemini", st.session_state[f"suggested_answer_{index}_{file_path}"], 
                             height=400, disabled=True, key=f"suggested_answer_{index}_{file_path}")
            except Exception as e:
                st.text_area("🤖 Câu trả lời đề xuất từ Gemini", str(e), 
                             height=400, disabled=True, key=f"suggested_answer_{index}_{file_path}")
        else:
            st.text_area("🤖 Câu trả lời đề xuất từ Gemini", st.session_state[f"suggested_answer_{index}_{file_path}"], 
                         height=400, disabled=True, key=f"suggested_answer_{index}_{file_path}")
