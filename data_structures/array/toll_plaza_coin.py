if __name__=="__main__":
    first_book_page=int(input())
    lines_in_first_book=int(input())
    second_book_pages=int(input())
    lines_in_second_book=int(input())
    speed_read=int(input())
    speed_write=int(input())
    time=int(input())
    operation=''
    page_number=0
    line_number=0
    if (first_book_page*lines_in_first_book)//speed_read<time:
        time-=(first_book_page*lines_in_first_book)//speed_read
        operation='WRITE'
        page_number=((time*speed_write)//lines_in_second_book)
        line_number=(time*speed_write)%lines_in_second_book
    else:
        operation="READ"
        page_number = ((time * speed_read) // lines_in_first_book)
        line_number = (time * speed_read) % lines_in_first_book
    print(operation,page_number,line_number)

# 100
# 10
# 500
# 6
# 8
# 4
# 145