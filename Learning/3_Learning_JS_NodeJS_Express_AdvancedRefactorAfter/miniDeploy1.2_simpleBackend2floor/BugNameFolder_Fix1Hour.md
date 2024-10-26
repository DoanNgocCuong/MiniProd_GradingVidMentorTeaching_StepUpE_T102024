
LỖI ĐẶT TÊN THƯ MỤC CÓ CHỨA DẤU CHẤM => ẢNH HƯỞNG ĐẾN ĐƯỜNG DẪN THƯ MỤC <Lỗi khi đi sâu vào cd, chứ cd nông thì không bị>

```bash bug 

PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor> cd ver1.1.0_Only_1fileJStoAPI
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor\ver1.1.0_Only_1fileJStoAPI> node -v
v20.18.0
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor\ver1.1.0_Only_1fileJStoAPI> cd test
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor\ver1.1.0_Only_1fileJStoAPI\test> node -v
Program 'node.exe' failed to run: The directory name is invalidAt line:1 char:1
+ node -v
+ ~~~~~~~.
At line:1 char:1
+ node -v
+ ~~~~~~~
    + CategoryInfo          : ResourceUnavailable: (:) [], ApplicationFailedException
    + FullyQualifiedErrorId : NativeCommandFailed

PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor\ver1.1.0_Only_1fileJStoAPI\test> cd ..   
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor\ver1.1.0_Only_1fileJStoAPI> cd test1
cd : Cannot find path 'D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&T
ask\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Expr 
ess_Deploy\miniDeploy1.2_simpleBackend2floor\ver1.1.0_Only_1fileJStoAPI\test1' because it does not       
exist.
At line:1 char:1
+ cd test1
+ ~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (D:\OneDrive - H...leJStoAPI\test1:String) [Set-Location]  
   , ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor\ver1.1.0_Only_1fileJStoAPI> cd ..
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor> cd test1
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor\test1> cd test2 
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor\test1\test2> node -v
v20.18.0
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1.2_simpleBackend2floor\test1\test2>
```

----------


### Sao fix rồi: tắt dấu chấm rồi vẫn bị;  => do lỗi ĐƯỜNG DẪN QUÁ DÀI => CHUYỂN RA VỊ TRÍ KHÁC LÀ ĐƯỢC

```bash
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1_2_simpleBackend2floor> cd ver1_2_0_Only_1fileJStoAPI
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1_2_simpleBackend2floor\ver1_2_0_Only_1fileJStoAPI> cd ..                     
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1_2_simpleBackend2floor> cd ver1_2_0_Only_1fileJStoAP 
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1_2_simpleBackend2floor\ver1_2_0_Only_1fileJStoAP> node -v
v20.18.0
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1_2_simpleBackend2floor\ver1_2_0_Only_1fileJStoAP> cd backend
PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1_2_simpleBackend2floor\ver1_2_0_Only_1fileJStoAP\backend> node -v   
Program 'node.exe' failed to run: The directory name is invalidAt line:1 char:1
+ node -v
+ ~~~~~~~.
At line:1 char:1
+ node -v
+ ~~~~~~~
    + CategoryInfo          : ResourceUnavailable: (:) [], ApplicationFailedException
    + FullyQualifiedErrorId : NativeCommandFailed

PS D:\OneDrive - Hanoi University of Science and Technology\ITE10-DS&AI-HUST\Learn&Task\PRODUCT_THECOACH\git2\MiniProduct_GradingMentorVideoTeaching_StepUpE_T102024\Learning_JS_NodeJS_Express_Deploy\miniDeploy1_2_simpleBackend2floor\ver1_2_0_Only_1fileJStoAP\backend>
```
