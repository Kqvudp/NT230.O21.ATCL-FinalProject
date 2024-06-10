#!/bin/bash

# Thư mục nguồn và đích
SRC_DIR="/home/kali/Documents/another-benign"
DEST_DIR="/home/kali/Documents/another-benign-packed-upx"

# Tạo thư mục đích nếu chưa tồn tại
mkdir -p $DEST_DIR

# Duyệt qua tất cả các tệp trong thư mục nguồn
for file in "$SRC_DIR"/*; do
  # Kiểm tra nếu là file
  if [ -f "$file" ]; then
    # Lấy tên tệp không có thư mục
    filename=$(basename "$file")
    # Nén tệp và lưu vào thư mục đích
    upx -9 --force -o "$DEST_DIR/$filename" "$file"
  fi
done

echo "All files have been packed and saved to $DEST_DIR"
