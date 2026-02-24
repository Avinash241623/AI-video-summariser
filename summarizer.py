from openai import OpenAI
import os
client = OpenAI(api_key="OPENAI_API_KEY")
def chunk_text(text, max_length=3000):
        chunks = []    
        while len(text) > max_length:
            chunks.append(text[:max_length])
            text = text[max_length:]
        chunks.append(text)
        return chunks
def summarize_text(text):
        chunks = chunk_text(text)
        summaries = []
        for chunk in chunks:
            response = client.chat.completions.create(model="gpt-4o-mini",            messages=[
                {"role": "system", "content": "You are a professional video summarizer."},
                {"role": "user", "content": f"""
Summarize the following transcript in a structured way:
1. Title
2. Key Points
3. Important Insights
4. Conclusion

Transcript:
{chunk}
"""}
            ]
        )
            summaries.append(response.choices[0].message.content)
        return "\n".join(summaries)