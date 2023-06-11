import camelot
import sys

arrs = sys.argv

page_s = arrs[2] # point out the pages and ranges like 1,2-10,...
file_path = arrs[1] # point out to the path
format = arrs[3] # format in which you want to extract your files such as: 'json', 'excel',
                 # 'html', 'markdown', or 'sqlite'.
                 
output_name = sys.argv[4]

def main():
    try:
        tables = camelot.read_pdf(file_path, pages=page_s)
        tables.export(output_name, f=format)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
