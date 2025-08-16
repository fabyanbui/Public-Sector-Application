# Thứ tự chạy file và tổ chức thư mục:

1. `setup.ipynb`: thiết lập môi trường Python (3.12.3)
2. `selenium_crawler.ipynb`: crawl toàn bộ các url tương ứng với mỗi bộ ngành và với mỗi phân loại (Công dân, Doanh nghiệp, Tổ chức khác). Kết quả thu được bao gồm các file là `{Bộ ngành}_link.csv`, `{Tổ chức}Tab_link.csv}` và thông tin bộ ngành `ministries.csv`
3. `link_detail_crawler.ipynb`: crawl toàn bộ thông tin chi tiết của từng câu hỏi ứng với mỗi url. Kết quả thu được bao gồm 2 file là `link_detail.csv` và `tthc_link.csv`. Vì bước này chạy lâu nên **copy** 2 bản dự phòng `link_detail copy.csv` và `raw_data/link_detail.csv`
4. `tthc_crawler.ipynb`: crawl toàn bộ thông tin chi tiết của từng thủ tục hành chính (tri thức) ứng với mỗi url đã thu được trước đó. Kết quả thu được bao gồm 2 file là `tthc_detail.csv` và `tthc_detail.json`. Vì bước này chạy lâu nên **copy** 2 bản dự phòng `tthc_detail copy.csv` và `raw_data/tthc_detail.csv`
5. `full_crawler.ipynb`: crawl toàn bộ những thông tin còn thiếu ở TTHC (vì nhận thấy rằng TTHC link bị lỗi ở một số dòng, đồng thời có cả link của những câu hỏi trong mục TTHC liên quan nên dẫn đến lỗi). Kết quả thu được bao gồm file `tthc_recrawl.csv` và bản **copy** `raw_data/tthc_recrawl.csv`
6. `link_type_extractor.ipynb`: merge hết tất cả các link câu hỏi, phân loại, bộ ngành vào chung một bảng. Kết quả thu được bao gồm file `link_type.csv` và bản **copy** `raw_data/link_type.csv`
7. `raw_data_aggregator.ipynb`: tổng hợp tất cả các thông tin đã crawl (bao gồm 4 file có bản copy ở trên). Kết quả thu được bao gồm 2 file là `raw_data/raw_link.csv` và `raw_data/raw_tthc.csv`

## Thông tin thêm về các file và đường dẫn:
- `raw_data/raw_link.csv` là raw data chứa các câu hỏi, mỗi dòng có một đường dẫn duy nhất tới câu hỏi tương ứng. Đồng thời, mỗi câu hỏi cũng sẽ có TTHC liên quan, feature này là một list chứa các đường dẫn tới TTHC liên quan tương ứng có trong file `raw_data/raw_tthc.csv` bên dưới
- `raw_data/raw_tthc.csv` là raw data chứa các TTHC (tri thức), mỗi dòng có một đường dẫn duy nhất tới TTHC liên quan tương ứng
- Thư mục `old_csv_test` chỉ là dùng để làm lại thử và phát triển thêm các file trong `Backup`

> Last updated date of raw data: 10/05/2025