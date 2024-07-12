def get_git_log(repo_url, file_path):
    try:
        os.chdir(repo_url)
        result = subprocess.run(["git", "log", "--follow", file_path], 
                                capture_output=True, text=True, check=True)
        print(result.stdout)
        commit_hashes = result.stdout.strip().split('\n')
        print(commit_hashes)
        return commit_hashes
    except subprocess.CalledProcessError as e:
        print(f"오류 발생: {e}")
def get_file_content_at_commit(repo_url, commit_hash, file_path):
    try:
        os.chdir(repo_url)
        subprocess.run(["git", "checkout", commit_hash], check=True)
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    
def get_c_function_infos(node, source_code):
        function_infos = {}

        def walk_tree(node):
            if node.type == 'function_definition':
                name_node = node.child_by_field_name('declarator').child_by_field_name('declarator')
                if name_node:
                    function_name = source_code[name_node.start_byte:name_node.end_byte].decode('utf-8')
                    function_infos[function_name] = (node.start_point[0], node.end_point[0])
                
                for child in node.children:
                    walk_tree(child)

            walk_tree(node)
            return function_infos
def get_java_function_infos(node, source_code):
    function_infos = {}

    def walk_tree(node):
        if node.type == 'method_declaration':
            name_node = node.child_by_field_name('name')
            if name_node:
                function_name = source_code[name_node.start_byte:name_node.end_byte].decode('utf-8')
                function_infos[function_name] = (node.start_point[0], node.end_point[0])
        
        for child in node.children:
            walk_tree(child)

    walk_tree(node)
    return function_infos