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