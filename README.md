# ROSを使用した簡単な足し算と引き算(正誤判定あり)
scripts内のprob.pyがパブリッシャ、ans.pyがサブスクライバとなっている。


# 実行方法
1. roscoreする。
2. prob.pyとans.pyを別々のターミナルで起動させる。
3. prob.pyで足し算、または引き算の問題が出力され、待機状態になる。
4. prob.pyで解答を入力すると、ans.pyに正誤が判定され出力される。
5. 正解なら問題が続き、不正解だとprob.pyの実行が終了される。


動作確認用動画
https://twitter.com/CitDaigo/status/1221780440853315584

# 参考資料
https://ryuichiueda.github.io/robosys2019/lesson12.html#/
