from langchain import serve
if __name__ == "__main__":
    serve.serve(host="0.0.0.0", port=8000)
