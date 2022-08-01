#XSS vs CSRF
#attack client vs attack server
#사이트 변조, 백도어 vs 요청 위조, 사용자 권한 이용

#xss 예시
# 사용자 입력에 <script> alert('xss arrack!')</script>

#Defense
#1 - 치환하기

#3.a태그 클릭시 id값에 따른 pageId 분기처리
form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    description = open('data/'+pageId,'r').read() #open함수로 내용 불러오기
    description = description.replace('<','&lt;') #XSS공격을 막기 위한 특수문자 치환
    description = description.replace('<','&gt;') #XSS공격을 막기 위한 특수문자 치환
 
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action= '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)  #delete버튼을 form방식으로 만든다
else :
    title = pageId = 'welcome'
    description = 'Welcome!'
    update_link = ''
    delete_action = ''

#2 HTML_Sanitizer 사용