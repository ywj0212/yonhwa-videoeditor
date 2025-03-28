# 연화 홍보부용 영상 편집 툴

## 사용 방법

## 빌드 설명

### MacOS
1. 개발자 인증서 발급은 공식 문서 참고
2. 사전 정보 입력
2.1. 정보 찾기
```zsh
security find-identity -p basic -v                                                                           
  1) XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX "Apple Development: JOHN DOE (XXXXXXXXXX)"
  2) XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX "Developer ID Application: JOHN DOE (XXXXXXXXXX)"
  ...
     N valid identities found
```
2.2. `Yonhwa Video Editor (MacOS).spec` (line 39)
```python
codesign_identity="Developer ID Application: JOHN DOE (XXXXXXXXXX)",
```
2.3. `resign_hook.py` (line 17)
```python
codesign_identity = "Apple Development: JOHN DOE (XXXXXXXXXX)"
```

3. 빌드
```bash
user@mac:/ $ pyinstaller Yonhwa\ Video\ Editor MacOS.spec
```
3.1. 서명 확인
```bash
user@mac:/ $ cd dist
user@mac:/dist $ codesign --verify --verbose=4 ./Yonhwa\ Video\ Editor.app   
./Yonhwa Video Editor.app: valid on disk
./Yonhwa Video Editor.app: satisfies its Designated Requirement
user@mac:/dist $ spctl -a -vvv -t install ./Yonhwa\ Video\ Editor.app 
./Yonhwa Video Editor.app: rejected
source=Unnotarized Developer ID
origin=Developer ID Application: JOHN DOE (XXXXXXXXXX)
```
3.2. 공증
```bash
user@mac:/dist $ xcrun notarytool store-credentials playbit-notarytool-password --team-id "개발자 팀 ID" --apple-id "개발자 이메일" --password "앱 비밀번호"
user@mac:/dist $ ditto -c -k --keepParent Yonhwa\ Video\ Editor.app Yonhwa\ Video\ Editor.app.zip
user@mac:/dist $ xcrun notarytool submit Yonhwa\ Video\ Editor.app.zip --keychain-profile "playbit-notarytool-password" --wait
user@mac:/dist $ xcrun stapler staple Yonhwa\ Video\ Editor.app
```
4. 확인
```bash
user@mac:/dist $ xcrun stapler validate Yonhwa\ Video\ Editor.app
user@mac:/dist $ spctl -a -vvv -t install ./Yonhwa\ Video\ Editor.app 
./Yonhwa Video Editor.app: accepted
source=Notarized Developer ID
origin=Developer ID Application: JOHN DOE (XXXXXXXXXX)
```

### Windows
```bash
user@windows:/ $ pyinstaller '.\Yonhwa Video Editor Windows.spec'
```