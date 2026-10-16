# Security Hub — 合并索引（cybersecurity-kb + hack-skills）

> 统一入口 `security-hub` 的组合索引。防御广度见 cybersecurity-kb，进攻深度见 hack-skills。

## A. cybersecurity-kb（防御 / 合规 / 取证，754 个技能）

完整按领域清单：`cybersecurity-kb/SKILLS_INDEX.md`

| 领域 | 数量 |
|---|---|
| cloud-security | 63 |
| threat-hunting | 56 |
| threat-intelligence | 50 |
| network-security | 43 |
| web-application-security | 42 |
| malware-analysis | 39 |
| digital-forensics | 37 |
| soc-operations | 33 |
| identity-access-management | 33 |
| container-security | 29 |
| security-operations | 28 |
| ot-ics-security | 28 |
| api-security | 28 |
| incident-response | 26 |
| vulnerability-management | 25 |
| red-teaming | 24 |
| penetration-testing | 20 |
| devsecops | 17 |
| zero-trust-architecture | 17 |
| endpoint-security | 17 |
| phishing-defense | 15 |
| cryptography | 15 |
| mobile-security | 13 |
| ransomware-defense | 13 |
| threat-detection | 7 |
| application-security | 4 |
| compliance-governance | 4 |
| supply-chain-security | 3 |
| deception-technology | 3 |
| ai-security | 2 |
| wireless-security | 2 |
| offensive-security | 2 |
| privacy-compliance | 2 |
| identity-and-access-management | 2 |
| red-team | 2 |
| identity-security | 1 |
| blockchain-security | 1 |
| firmware-security | 1 |
| social-engineering-defense | 1 |
| data-protection | 1 |
| zero-trust | 1 |
| ot-security | 1 |
| firmware-analysis | 1 |
| purple-team | 1 |
| governance-risk-compliance | 1 |

## B. hack-skills（进攻 / 赏金 / CTF，102 个技能）

主入口 `hack` → 6 个分类路由 → 95 个深度主题。

### 6 个分类路由（category routers）

- `recon-for-sec`
- `api-sec`
- `auth-sec`
- `injection-checking`
- `file-access-vuln`
- `business-logic-vuln`

### 95 个深度主题（deep topics，按字母序）

- `401-403-bypass-techniques`
- `active-directory-acl-abuse`
- `active-directory-certificate-services`
- `active-directory-kerberos-attacks`
- `ai-ml-security`
- `android-pentesting-tricks`
- `anti-debugging-techniques`
- `api-auth-and-jwt-abuse`
- `api-authorization-and-bola`
- `api-recon-and-docs`
- `arbitrary-write-to-rce`
- `authbypass-authentication-flaws`
- `binary-protection-bypass`
- `browser-exploitation-v8`
- `business-logic-vulnerabilities`
- `classical-cipher-analysis`
- `clickjacking`
- `cmdi-command-injection`
- `code-obfuscation-deobfuscation`
- `container-escape-techniques`
- `cors-cross-origin-misconfiguration`
- `crlf-injection`
- `csp-bypass-advanced`
- `csrf-cross-site-request-forgery`
- `csv-formula-injection`
- `dangling-markup-injection`
- `defi-attack-patterns`
- `dependency-confusion`
- `deserialization-insecure`
- `dns-rebinding-attacks`
- `email-header-injection`
- `expression-language-injection`
- `format-string-exploitation`
- `ghost-bits-cast-attack`
- `graphql-and-hidden-parameters`
- `hash-attack-techniques`
- `heap-exploitation`
- `http-host-header-attacks`
- `http-parameter-pollution`
- `http2-specific-attacks`
- `idor-broken-object-authorization`
- `insecure-source-code-management`
- `ios-pentesting-tricks`
- `jndi-injection`
- `jwt-oauth-token-attacks`
- `kernel-exploitation`
- `kubernetes-pentesting`
- `lattice-crypto-attacks`
- `linux-lateral-movement`
- `linux-privilege-escalation`
- `linux-security-bypass`
- `llm-prompt-injection`
- `macos-process-injection`
- `macos-security-bypass`
- `memory-forensics-volatility`
- `mobile-ssl-pinning-bypass`
- `network-protocol-attacks`
- `nosql-injection`
- `ntlm-relay-coercion`
- `oauth-oidc-misconfiguration`
- `open-redirect`
- `path-traversal-lfi`
- `prototype-pollution`
- `prototype-pollution-advanced`
- `race-condition`
- `recon-and-methodology`
- `request-smuggling`
- `reverse-shell-techniques`
- `rsa-attack-techniques`
- `saml-sso-assertion-attacks`
- `sandbox-escape-techniques`
- `smart-contract-vulnerabilities`
- `sqli-sql-injection`
- `ssrf-server-side-request-forgery`
- `ssti-server-side-template-injection`
- `stack-overflow-and-rop`
- `steganography-techniques`
- `subdomain-takeover`
- `symbolic-execution-tools`
- `symmetric-cipher-attacks`
- `traffic-analysis-pcap`
- `tunneling-and-pivoting`
- `type-juggling`
- `unauthorized-access-common-services`
- `upload-insecure-files`
- `vm-and-bytecode-reverse`
- `waf-bypass-techniques`
- `web-cache-deception`
- `websocket-security`
- `windows-av-evasion`
- `windows-lateral-movement`
- `windows-privilege-escalation`
- `xslt-injection`
- `xss-cross-site-scripting`
- `xxe-xml-external-entity`

## C. 速查路由表

| 想做的事 | 调哪个 |
|---|---|
| 威胁狩猎/取证/IR/合规 | cybersecurity-kb (SKILLS_INDEX.md) |
| 云安全审计 AWS/Azure/GCP/K8s | cybersecurity-kb → cloud-security / container-security |
| 恶意代码/移动端分析 | cybersecurity-kb → malware-analysis |
| Web/API 漏洞利用 | hack → injection-checking / api-sec / file-access-vuln |
| 认证授权 OAuth/JWT/SAML/IDOR | hack → auth-sec / jwt-oauth-token-attacks / oauth-oidc-misconfiguration |
| 提权 Linux/Windows/AD | hack → linux-privilege-escalation / windows-privilege-escalation / active-directory-kerberos-attacks |
| 逆向/二进制/Pwn | hack → vm-and-bytecode-reverse / heap-exploitation / stack-overflow-and-rop |
| 密码学/区块链/AI安全 | hack → rsa-attack-techniques / smart-contract-vulnerabilities / llm-prompt-injection |
| 侦察先从哪下手 | hack → recon-for-sec |

## D. 许可与署名

- cybersecurity-kb: Apache-2.0（mukul975/Anthropic-Cybersecurity-Skills，fork ctkqiang/CybersecuritySkills）
- hack-skills: MIT（yaklang/hack-skills，fork strivepan-svg/hack-skills，Copyright 2026 VillanCh）

> 使用须严格限定在授权测试、合法研究、防御验证、赏金规则范围内。