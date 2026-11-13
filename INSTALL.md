# SlimWeb Plugin 安裝入口

把本頁網址和網站後台提供的「完整 MCP URL」一起交給 AI，即可請 AI 協助安裝 MCP + Skill。Plugin 將兩者包成一套，Google 登入與授權仍由本人完成。本專案提供公開原始碼及自管 marketplace 清單，**尚未宣稱上架任何官方公開 Plugin 市集**。

- 統一入口：https://github.com/ericchen1972/slimweb-skill/blob/main/INSTALL.md
- AI 可讀原文：https://raw.githubusercontent.com/ericchen1972/slimweb-skill/main/INSTALL.md
- 安裝目標：一律使用網站後台提供的完整 MCP URL，保留 `?domain=...` 等查詢參數，不在此文件指定任何網站或預設端點。
- 套件選擇：讀取 marketplace entry 指向的 Plugin `mcp.json`，以完整 URL 比對；沒有完全相符的套件就使用下方產生器，不能只依名稱猜測。

## AI 外掛自動安裝（推薦）

ChatGPT 用戶請進入 Codex 模式，並授予 Codex 完全存取權後，複製下方文字貼給 AI。Google 登入與授權由本人完成。

```text
請依照 https://raw.githubusercontent.com/ericchen1972/slimweb-skill/main/INSTALL.md 安裝 SlimWeb MCP + Skill。
目標完整 MCP URL：［貼上此網站後台提供的完整 HTTPS MCP URL］
先辨識目前 AI 宿主與支援的 Plugin、MCP、Skill 安裝方式，檢查已有的 SlimWeb 連線與 Skill，避免重複安裝、保留其他站台設定。若完整目標 URL 尚未提供，先向我取得，不要自行猜測或預設端點。獨立版必須保留 domain 等查詢參數。
優先使用宿主支援的 Plugin 匯入／本機 marketplace 安裝；無此能力就使用 MCP + Skill 分開安裝。不要宣稱 ChatGPT 網頁一定能直接安裝 GitHub 本機 Plugin，也不要宣稱已上架官方市集。
設定後引導我本人完成 Google OAuth 授權，不收集帳密、不內嵌 token、secret 或固定 OAuth client ID。若遇 invalid_client、Client not found 或舊 client 過期，清除這個目標連線的舊授權，透過 discovery 與 DCR 重新註冊並登入，不要重用別人的 client ID。
最後呼叫 slimweb_sites_list，核對可存取的網站與目標。只在實際成功後回報已連線；未完成授權或沒有權限就說明目前停在哪一步。
```

## AI 安裝流程

1. 確認宿主（Codex／ChatGPT desktop／ChatGPT web／Claude Code／其他）及目前版本的支援方式。讀取既有設定，依完整 URL 比對連線；同一伺服器名稱可能對應不同網站，不可只憑名稱覆蓋。檢查既有 `slimweb-mcp` Skill 路徑與來源，保留使用者修改；已有 Plugin 就不要再安裝同一份裸 MCP 和 Skill。
2. 選擇 `mcp.json` 中 URL 與目標完整 URL 完全一致的 Plugin，並從其 marketplace entry 取得安裝名稱。沒有相符套件時使用下方產生器。Plugin 1.1.0 起只包含精簡的 `skills/slimweb-mcp/SKILL.md` 啟動指南；完整操作文件由已連線 MCP 的 `slimweb_guides_get` 提供，不在 Plugin 另附 `references/`。
3. 使用宿主實際支援的匯入方式。可安裝本機 Plugin 的 Codex／ChatGPT desktop 使用 `.agents/plugins/marketplace.json`；其中 `source.path` 相對於 marketplace 根目錄。本庫是 repo marketplace，可在可信任的本機 checkout 中使用；其他專案或個人 marketplace 必須調整到實際 Plugin 位置，合併而非覆蓋既有清單。需要時重啟宿主、啟用所選 Plugin。啟用方式依宿主文件與版本確認。
4. Claude Code 可先使用 `/plugin marketplace add ericchen1972/slimweb-skill`，再從清單選擇已核對完整 URL 的 Plugin。自訂套件可用 `claude --plugin-dir /absolute/path/to/generated-plugin` 進行本機載入；持久安裝使用宿主支援的 marketplace 流程。只安裝符合目標的一個。
5. ChatGPT web 的能力取決於帳號、工作區及管理員設定。若具有 Plugin GitHub 匯入或管理員流程，使用該流程並選取正確子目錄；若不支援此 repo 的本機 marketplace，改用可用的遠端 MCP／App 設定與 Skill／知識檔案方式，不要把貼上一個網址說成已完成安裝。安裝本機 Skill、上傳 Knowledge 本身不會建立 MCP 連線。
6. 由使用者在瀏覽器親自完成 Google OAuth。使用 discovery 與新的 DCR，不將憑證寫入 repo。授權後確認工具可用，呼叫 `slimweb_sites_list` 並確認網站身份。安裝驗證不需要建立訂單、付款、發送訊息或修改網站。

## Codex 安裝與更新

Codex CLI 支援此 repo marketplace 時，優先使用宿主命令，不直接拼接 `config.toml`：

```sh
codex plugin marketplace add ericchen1972/slimweb-skill
```

加入來源後，讀取 `.agents/plugins/marketplace.json` 的 `plugins[]`；依各 entry 的 `source.path` 找到其 Plugin，再檢查 `mcp.json` 的完整 URL。只有 URL 與後台提供的目標完全一致，才能取用該 entry 的 `name` 與 marketplace 的 `name` 組成安裝 selector。沒有完全相符的套件時，先用下方產生器建立目標套件，再加入本機 marketplace。

以下只是不可直接執行的語法佔位說明，必須先以剛才核對出的實際值替換：

```text
codex plugin add <MATCHED_PLUGIN_NAME>@<MARKETPLACE_NAME> --json
```

更新已安裝的舊套件：先檢查版本與完整 URL，使用宿主的 marketplace 更新命令更新對應來源，再以已核對的 selector 重新安裝。首次切換此架構時，確認安裝版本為 **1.1.0 或更新版本**，並重新載入宿主後驗證。不要只改 Plugin cache，否則重新安裝會覆蓋修改。不同目標不得共用或互相覆蓋設定。

### 舊版 1.0.0 相容性與重複設定

Codex 0.167.0-alpha.4.1 的 Plugin MCP 解析器會拒絕 server 裡的 `extensions`，錯誤是 `unknown field extensions, expected url or headers`。1.0.1 改為可攜的 `type: streamable-http` + 原始 `url`，由 MCP server 的 OAuth discovery 與 DCR 啟動授權，不在套件硬編碼 client ID。Plugin 安裝／Skill 載入不等於 MCP 已連線；必須實際取得工具並成功呼叫 `slimweb_sites_list`。

若之前因相容問題額外新增了裸 MCP，先確認新版 **Plugin 本身的 MCP** 能載入並完成登入及網站清單，再移除指向完全相同 URL 的裸 MCP，避免重複工具。保留不同網站、不同 domain 或其他端點的既有連線。若仍需分開安裝，明確回報正在使用相容方式，不要宣稱 Plugin MCP 已驗證成功。

已有獨立 `slimweb-mcp` Skill 時，保留使用者修改及檔案；Plugin Skill 正常載入後才停用重複 Skill。若確實必須修改 TOML，先建立候選內容，用 TOML parser 驗證整份候選設定，再以原子替換寫入；路徑必須是有引號的字串，避免 shell 多層引號破壞設定。不得用覆蓋整份設定的方式移除其他服務。

## Codex 手動安裝 MCP

手動流程只建立 MCP 連線；完整 Skill 仍請使用上方自動安裝，或下方分開安裝方式。

1. 進入 **設定 → 外掛程式**。
2. 點擊 **新增 → 新增 MCP 伺服器**。
3. 名稱輸入 **SlimWeb**，類型選擇 **可串流 HTTP**。
4. URL 貼上網站後台提供的**完整 MCP URL**（含 `domain` 等查詢參數），不要貼 GitHub 的安裝文件或 Plugin 儲存庫網址。截圖中的 URL 只是示例，請複製目前網站自己的 URL。
5. 儲存並由本人完成 Google 登入與授權；重新載入後請 AI 呼叫 `slimweb_sites_list`，確認網站身份。

## 分開安裝的相容方式

保留原本的獨立 MCP + Skill 流程。把**目標完整 URL**填入宿主的遠端 Streamable HTTP MCP 設定，使用 OAuth；各宿主的設定鍵不同，請依其支援格式調整。Claude Code 可使用：

```sh
claude mcp add --transport http slimweb-target 'https://YOUR-HOST/mcp?domain=YOUR-DOMAIN'
```

此為佔位範例，不能直接執行；改成網站提供的精確 URL。Codex 等宿主也應使用實際 URL，不要貼入 Claude 的格式。

分開安裝時，只將根目錄的精簡 [SKILL.md](SKILL.md) 放入宿主的 `slimweb-mcp/` Skill 目錄；例如 Codex 的 `~/.agents/skills/slimweb-mcp/`（舊版本可能使用 `~/.codex/skills/`）。先檢查已有版本，避免兩處重複載入；保留使用者修改與檔案，不把舊 references 當作連線失敗時的替代操作指南。Skill 安裝與 MCP 授權是各自必須完成的步驟。

## 精簡 Plugin 與即時指南

從舊版完整 Skill 升到 **1.1.0** 需要更新一次 Plugin。之後每個新 SlimWeb 任務先呼叫 `slimweb_guides_get`（`topic: index`），依回傳的 `guide_version` 讀取 `overview` 與相關主題。日常操作文件更新由 MCP 服務部署後提供，不必為每次文件修改重裝 Plugin；本機 bootstrap 本身若變更仍需正常更新套件。

這不是自動升級 AI Client、Plugin binary 或執行更新腳本。MCP 新增工具後，部分宿主需要重新整理工具清單、重新連線或重啟。指南工具不存在、授權失敗或必要指南讀取失敗時，AI 應停止網站寫入，說明原因並在連線修復後重試；不能改用舊本機文件或猜測工具。

指南只有通用文件，不授予網站操作權限；登入、選站、目前工具 schema 與人工確認仍是執行邊界。

## 維護與其他獨立版產生器

根目錄 `SKILL.md` 是精簡 bootstrap 的唯一來源；`guides/overview.md` 與 `references/*.md` 是服務端操作文件的正式來源。`plugins/` 是可重建的發佈副本，不直接修改。

```sh
python3 -m unittest discover -s tests -v
python3 scripts/build-plugins.py --refresh-generated
python3 scripts/export-guides.py --output /absolute/path/to/new-guide-export
python3 scripts/build-plugins.py --name slimweb-target --url 'https://YOUR-HOST/mcp?domain=YOUR-DOMAIN' --output /absolute/path/to/new-plugin
```

上面的路徑與 `YOUR-HOST`／`YOUR-DOMAIN` 是佔位範例，必須替換後使用。指南匯出要求明確、尚不存在的輸出目錄，僅匯出正式 Markdown 與決定性的 `manifest.json`（版本由內容雜湊產生），不讀取憑證或其他本機檔案。將匯出結果發佈到 MCP 服務後才會更新已連線客戶端可讀的指南。

自訂指令必須提供 `--name`、`--url` 和 `--output`，不會預設端點。首次輸出要求不存在的目錄；`--refresh-generated` 只更新由本產生器建立、名稱與 URL 完全一致的目錄，保留額外使用者檔案，拒絕覆寫不相關資料夾。更新到精簡版本會以固定的舊發佈 SHA-256 或目前正式來源辨識未修改的 generated references 並移除；不會因新版指南內容變動而誤判舊發佈副本已被使用者修改。若該目錄有使用者修改、未知檔案或 symlink 則拒絕更新，先保留並人工處理。不要將輸出指向來源 repo 或既有安裝目錄。更新後重新安裝／同步，並依宿主要求重新載入。

## 格式與目前驗證範圍

- 根 `plugin.json`、`mcp.json`、`skills/` 採 Agent Plugins 佈局；MCP 使用 `streamable-http` 與完整 `url`，不放入目前 Codex 無法解析的 `extensions`；OAuth discovery 與 DCR 由宿主管理。
- `.claude-plugin/plugin.json` 及 `.mcp.json` 提供 Claude 相容格式，HTTP transport 為 `http`，由宿主管理 OAuth。
- `.agents/plugins/marketplace.json` 和 `.claude-plugin/marketplace.json` 為各宿主不同格式的自管清單，不代表公開市集審核或上架。
- 1.0.1 修正 Codex 已實際回報的 `extensions` 解析錯誤；不因文件列出某個 extension 就假設每個宿主版本都能解析。自動測試限制可攜 HTTP server 的欄位，避免再次產生此不相容設定。
- 自動化測試涵蓋 URL 保留、無效輸入拒絕、資料夾保護、精簡 Skill、舊產物遷移保護、指南匯出雜湊與可重建一致性。這不等同每個宿主已完成真實 Google 授權；最終以該宿主實際連線及 `slimweb_sites_list` 成功為準。
- 2026-11-14：Codex 0.167.0-alpha.4.1 的 Plugin 1.0.1 已完成真實 Google 授權；移除同 URL 的裸 MCP 後，原生 app-server 確認 MCP 來自已安裝 Plugin、工具載入無錯誤，且唯讀 `slimweb_sites_list` 呼叫成功。此為已測試宿主與目標的結果；其他環境仍須個別驗證。公開安裝文件不記錄使用者帳號、網站名稱或網站清單。

官方格式參考：[OpenAI Plugin 包裝](https://developers.openai.com/plugins/build/plugins)、[Agent Plugins Manifest Schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)、[MCP Schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json)、[Claude Plugin reference](https://code.claude.com/docs/en/plugins-reference)。
