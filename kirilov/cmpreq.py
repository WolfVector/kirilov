FROM_STDIN = 256
FROM_FILE = 257

from kirilov._util import get_requirements, cmpreq, pip_freeze
import argparse

class CmpReq:
    def __init__(self) -> None:
        self.sources = []
    
    def add_src(self, data='') -> None:
        from_src = FROM_FILE

        if len(self.sources) >= 2:
            raise Exception("Error, only two files can be compared")
        elif data != '-':
            data = get_requirements(data)
        else:
            data = pip_freeze()
            from_src = FROM_STDIN
        
        self.sources.append({ "data": data, "from_src": from_src })
    
    def cmp(self, output=True, download=False, path='') -> None:
        if len(self.sources) < 2:
            raise Exception("ERROR, you must provide two sources")
        
        file1 = self.sources[0]
        file2 = self.sources[1]

        if file1["from_src"] == FROM_STDIN and file2["from_src"] == FROM_STDIN:
            file2["data"] = []

        cmpreq(file1["data"], file2["data"], output, download, path)

def main():   
    parser = argparse.ArgumentParser(description="List and download new requirements")
    parser.add_argument("-op", "--output", type=bool, default=True, help="Output a file with the new requirements?. Default True")
    parser.add_argument("-d", "--download", type=bool, default=False, help="Download the new requirements? Default false")
    parser.add_argument("-p", "--path", type=str, default="./downloads", help="The path of the download directory. Default ./downloads")
    parser.add_argument("-f1", "--file1", type=str, default="-", help="Path to the requirements file or '-'. The meaning of '-' is pip freeze")
    parser.add_argument("-f2", "--file2", type=str, default="-", help="Path to the requirements file or '-'. The meaning of '-' is pip freeze")

    args = parser.parse_args()

    cmp = CmpReq()
    cmp.add_src(args.file1)
    cmp.add_src(args.file2)

    cmp.cmp(output=args.output, download=args.download, path=args.path)


if __name__ == '__main__':
    main()
