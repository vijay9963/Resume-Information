prompt_template = """
Extract information from the resume.

Return ONLY a JSON object.

Do not add:
- markdown
- explanations
- comments
- ```json

Resume:
{resume_text}

Output format:

{{
"name":"",
"email":"",
"phone":"",
"skills":[],
"total_experience_years":""
}}
"""