from crewai_tools import YoutubeVideoSearchTool, YoutubeChannelSearchTool, PDFSearchTool


# Targeted search within a specific Youtube video's content

Yt_searchTool = YoutubeVideoSearchTool(
    #  youtube_video_url='https://youtube.com/watch?v=example',#optional if you want to target a specific video
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        # embedder=dict(
        #     provider="google", # or openai, ollama, ...
        #     config=dict(
        #         model="models/embedding-001",
        #         task_type="retrieval_document",
        #         # title="Embeddings",
        #     ),
        # ),
    )
)



#  Initialize the tool with a specific Youtube channel handle to target your search

Yt_ChannelTool = YoutubeChannelSearchTool(
    # youtube_channel_handle='example',#optional if you want to target a specific channel
    
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        # embedder=dict(
        #     provider="google", # or openai, ollama, ...
        #     config=dict(
        #         model="models/embedding-001",
        #         task_type="retrieval_document",
        #         # title="Embeddings",
        #     ),
        # ),
    )
)



PDFtool = PDFSearchTool(
    # pdf_url='https://example.com/example.pdf',#optional if you want to target a specific pdf
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
         ),
    #     embedder=dict(
    #         provider="google", # or openai, ollama, ...
    #         config=dict(
    #             model="models/embedding-001",
    #             task_type="retrieval_document",
    #             # title="Embeddings",
    #         ),
    #     ),
    )
)

