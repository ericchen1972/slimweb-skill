# SlimWeb Plugin 安裝入口

把本頁網址和網站後台提供的「完整 MCP URL」一起交給 AI，即可請 AI 協助安裝 MCP + Skill。Plugin 將兩者包成一套，Google 登入與授權仍由本人完成。本專案提供公開原始碼及自管 marketplace 清單，**尚未宣稱上架任何官方公開 Plugin 市集**。

- 統一入口：https://github.com/ericchen1972/slimweb-skill/blob/main/INSTALL.md
- AI 可讀原文：https://raw.githubusercontent.com/ericchen1972/slimweb-skill/main/INSTALL.md
- SaaS Plugin：[plugins/saas](plugins/saas)，MCP URL：`https://slimweb-mcp-aakwcbp2ca-de.a.run.app/mcp`
- 陸玖獨立版 Plugin：[plugins/lujiu](plugins/lujiu)，MCP URL：`https://slimweb-standalone-mcp-27587628711.asia-east1.run.app/mcp?domain=lujiu.com.tw`
- 其他獨立版：使用該網站後台提供的完整 URL，保留 `?domain=...` 等查詢參數；不可改用 SaaS URL。

## AI 外掛自動安裝（推薦）

ChatGPT 用戶請進入 Codex 模式，並授予 Codex 完全存取權後，複製下方文字貼給 AI。Google 登入與授權由本人完成。

```text
請依照 https://raw.githubusercontent.com/ericchen1972/slimweb-skill/main/INSTALL.md 安裝 SlimWeb MCP + Skill。
目標完整 MCP URL：［貼上此網站後台提供的完整 HTTPS MCP URL］
先辨識目前 AI 宿主與支援的 Plugin、MCP、Skill 安裝方式，檢查已有的 SlimWeb 連線與 Skill，避免重複安裝、保留其他站台設定。若完整目標 URL 尚未提供，先向我取得，不要自行猜測或預設成 SaaS。獨立版必須保留 domain 等查詢參數。
優先使用宿主支援的 Plugin 匯入／本機 marketplace 安裝；無此能力就使用 MCP + Skill 分開安裝。不要宣稱 ChatGPT 網頁一定能直接安裝 GitHub 本機 Plugin，也不要宣稱已上架官方市集。
設定後引導我本人完成 Google OAuth 授權，不收集帳密、不內嵌 token、secret 或固定 OAuth client ID。若遇 invalid_client、Client not found 或舊 client 過期，清除這個目標連線的舊授權，透過 discovery 與 DCR 重新註冊並登入，不要重用別人的 client ID。
最後呼叫 slimweb_sites_list，核對可存取的網站與目標。只在實際成功後回報已連線；未完成授權或沒有權限就說明目前停在哪一步。
```

## AI 安裝流程

1. 確認宿主（Codex／ChatGPT desktop／ChatGPT web／Claude Code／其他）及目前版本的支援方式。讀取既有設定，依完整 URL 比對連線；同一伺服器名稱可能對應不同網站，不可只憑名稱覆蓋。檢查既有 `slimweb-mcp` Skill 路徑與來源，保留使用者修改；已有 Plugin 就不要再安裝同一份裸 MCP 和 Skill。
2. 選擇與完整 URL 相符的 Plugin。SaaS 與 lujiu 可用本庫生成的資料夾。其他獨立版使用下方產生器。Plugin 內 `skills/slimweb-mcp/` 包含完整 `SKILL.md` 與全部 `references/`；勿只複製一個入口檔案。
3. 使用宿主實際支援的匯入方式。可安裝本機 Plugin 的 Codex／ChatGPT desktop 使用 `.agents/plugins/marketplace.json`；其中 `source.path` 相對於 marketplace 根目錄。本庫是 repo marketplace，可在可信任的本機 checkout 中使用；其他專案或個人 marketplace 必須調整到實際 Plugin 位置，合併而非覆蓋既有清單。需要時重啟宿主、啟用所選 Plugin。啟用方式依宿主文件與版本確認。
4. Claude Code 可先使用 `/plugin marketplace add ericchen1972/slimweb-skill`，再選擇 `/plugin install slimweb-saas@slimweb` 或 `/plugin install slimweb-lujiu@slimweb`。只安裝符合目標的一個。其他獨立版可用 `claude --plugin-dir /absolute/path/to/generated-plugin` 進行本機載入；持久安裝使用宿主支援的 marketplace 流程。
5. ChatGPT web 的能力取決於帳號、工作區及管理員設定。若具有 Plugin GitHub 匯入或管理員流程，使用該流程並選取正確子目錄；若不支援此 repo 的本機 marketplace，改用可用的遠端 MCP／App 設定與 Skill／知識檔案方式，不要把貼上一個網址說成已完成安裝。安裝本機 Skill、上傳 Knowledge 本身不會建立 MCP 連線。
6. 由使用者在瀏覽器親自完成 Google OAuth。使用 discovery 與新的 DCR，不將憑證寫入 repo。授權後確認工具可用，呼叫 `slimweb_sites_list` 並確認網站身份。安裝驗證不需要建立訂單、付款、發送訊息或修改網站。

## Codex 安裝與更新

Codex CLI 支援此 repo marketplace 時，優先使用宿主命令，不直接拼接 `config.toml`：

```sh
codex plugin marketplace add ericchen1972/slimweb-skill
codex plugin add slimweb-saas@slimweb --json
```

上面第二行只適用 SaaS 完整 URL；陸玖改為 `codex plugin add slimweb-lujiu@slimweb --json`。其他單機版先使用下方產生器建立與完整 URL 完全相符的 Plugin，再加入該本機 marketplace；不得把單機版改連 SaaS。

更新已安裝的舊套件：先檢查版本與 URL，使用 `codex plugin marketplace upgrade slimweb` 更新來源，再重新安裝對應 Plugin（`codex plugin add slimweb-saas@slimweb --json`，陸玖使用其對應名稱）。確認安裝版本為 **1.0.1 或更新版本**，並重新載入宿主後驗證。不要只改 Plugin cache，否則重新安裝會覆蓋修改。

### 舊版 1.0.0 相容性與重複設定

Codex 0.167.0-alpha.4.1 的 Plugin MCP 解析器會拒絕 server 裡的 `extensions`，錯誤是 `unknown field extensions, expected url or headers`。1.0.1 改為可攜的 `type: streamable-http` + 原始 `url`，由 MCP server 的 OAuth discovery 與 DCR 啟動授權，不在套件硬編碼 client ID。Plugin 安裝／Skill 載入不等於 MCP 已連線；必須實際取得工具並成功呼叫 `slimweb_sites_list`。

若之前因相容問題額外新增了裸 MCP，先確認新版 **Plugin 本身的 MCP** 能載入並完成登入及網站清單，再移除指向完全相同 URL 的裸 MCP，避免重複工具。保留不同網站、不同 domain 或其他端點的既有連線。若仍需分開安裝，明確回報正在使用相容方式，不要宣稱 Plugin MCP 已驗證成功。

已有獨立 `slimweb-mcp` Skill 時，保留使用者修改及檔案；Plugin Skill 正常載入後才停用重複 Skill。若確實必須修改 TOML，先建立候選內容，用 TOML parser 驗證整份候選設定，再以原子替換寫入；路徑必須是有引號的字串，避免 shell 多層引號破壞設定。不得用覆蓋整份設定的方式移除其他服務。

## Codex 手動安裝 MCP

手動流程只建立 MCP 連線；完整 Skill 仍請使用上方自動安裝，或下方分開安裝方式。

1. 進入 **設定 → 外掛程式**。
2. 點擊 **新增 → 新增 MCP 伺服器**。
3. 名稱輸入 **SlimWeb**，類型選擇 **可串流 HTTP**。
4. URL 貼上網站後台提供的**完整 MCP URL**（含 `domain` 等查詢參數），不要貼 GitHub 的安裝文件或 Plugin 儲存庫網址。截圖中的 SaaS URL 只是示例，其他網站請複製各自的 URL。
5. 儲存並由本人完成 Google 登入與授權；重新載入後請 AI 呼叫 `slimweb_sites_list`，確認網站身份。

## 分開安裝的相容方式

保留原本的獨立 MCP + Skill 流程。把**目標完整 URL**填入宿主的遠端 Streamable HTTP MCP 設定，使用 OAuth；各宿主的設定鍵不同，請依其支援格式調整。Claude Code 可使用：

```sh
claude mcp add --transport http slimweb-target 'https://YOUR-HOST/mcp?domain=YOUR-DOMAIN'
```

此為佔位範例，不能直接執行；改成網站提供的精確 URL。Codex 等宿主也應使用實際 URL，不要貼入 Claude 的格式。

將根目錄的 [SKILL.md](SKILL.md) 與完整 [references/](references/) 一起複製到宿主的 Skill 目錄；例如 Codex 的 `~/.agents/skills/slimweb-mcp/`（舊版本可能使用 `~/.codex/skills/`）。先檢查已有版本，避免兩處重複載入。支援 Knowledge 的宿主可使用 [chatgpt-knowledge/slimweb-mcp-ai-guide.md](chatgpt-knowledge/slimweb-mcp-ai-guide.md)，並依宿主支援加入參考檔。知識上傳與 MCP 授權是各自必須完成的步驟。

## 維護與其他獨立版產生器

根目錄 `SKILL.md` 與 `references/` 是唯一維護來源；`plugins/` 是可重建的發佈副本，不直接修改。

```sh
python3 -m unittest discover -s tests -v
python3 scripts/build-plugins.py --refresh-generated
python3 scripts/build-plugins.py --name slimweb-myshop --url 'https://YOUR-HOST/mcp?domain=YOUR-DOMAIN' --output /absolute/path/to/new-plugin
```

自訂指令必須提供 `--name`、`--url` 和 `--output`，不會默認 SaaS。首次輸出要求不存在的目錄；`--refresh-generated` 只更新由本產生器建立、名稱與 URL 完全一致的目錄，保留額外使用者檔案，拒絕覆寫不相關資料夾。不要將輸出指向來源 repo 或既有安裝目錄。更新後重新安裝／同步，並依宿主要求重新載入。

## 格式與目前驗證範圍

- 根 `plugin.json`、`mcp.json`、`skills/` 採 Agent Plugins 佈局；MCP 使用 `streamable-http` 與完整 `url`，不放入目前 Codex 無法解析的 `extensions`；OAuth discovery 與 DCR 由宿主管理。
- `.claude-plugin/plugin.json` 及 `.mcp.json` 提供 Claude 相容格式，HTTP transport 為 `http`，由宿主管理 OAuth。
- `.agents/plugins/marketplace.json` 和 `.claude-plugin/marketplace.json` 為各宿主不同格式的自管清單，不代表公開市集審核或上架。
- 1.0.1 修正 Codex 已實際回報的 `extensions` 解析錯誤；不因文件列出某個 extension 就假設每個宿主版本都能解析。自動測試限制可攜 HTTP server 的欄位，避免再次產生此不相容設定。
- 自動化測試涵蓋 URL 保留、無效輸入拒絕、資料夾保護、完整參考檔複製與可重建一致性。這不等同每個宿主已完成真實 Google 授權；最終以該宿主實際連線及 `slimweb_sites_list` 成功為準。

官方格式參考：[OpenAI Plugin 包裝](https://developers.openai.com/plugins/build/plugins)、[Agent Plugins Manifest Schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)、[MCP Schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json)、[Claude Plugin reference](https://code.claude.com/docs/en/plugins-reference)。
