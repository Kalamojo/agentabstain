from huggingface_hub import snapshot_download


if __name__ == "__main__":
    snapshot_download('antiquality/agentabstain', repo_type='dataset', local_dir='data')

