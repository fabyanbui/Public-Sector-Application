# Thứ tự chạy file và tổ chức thư mục

- Thiết lập lại môi trường Python (3.12.3) bằng setup.ipynb

- Copy raw_link.csv từ Rework/raw_data/raw_link.csv
- Copy raw_tthc.csv từ Rework/raw_data/raw_tthc.csv

- Chạy file preprocess_1.ipynb
> preprocess_1.csv

- Chạy file preprocess_2.ipynb 
(lấy dữ liệu từ preprocess_1.csv)
> preprocess_2.csv

- Chạy file preprocess_3.ipynb 
(lấy dữ liệu từ preprocess_2.csv)
> preprocess_3.csv, missing_ministry.csv

- Copy preprocessed_link.csv từ preprocess_3.csv

