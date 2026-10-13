---
title: "How to Fix ERR_CONNECTION_RESET Error in Google Chrome"
description: "Encountering the ERR_CONNECTION_RESET error in Google Chrome? Read our complete step-by-step troubleshooting guide to fix it quickly."
tags: ["Google Chrome", "Troubleshooting"]
---

## Why does the ERR_CONNECTION_RESET happen?

The **ERR_CONNECTION_RESET** error in Google Chrome means the connection between your browser and the website's server was unexpectedly interrupted before the page could load. Instead of receiving data, Chrome detects that the connection was forcibly closed, often resulting in the frustrating "This site can't be reached" message.

In most cases, this issue stems from a misconfigured **network proxy** or corrupted **browser cache and cookies**. A proxy server that is enabled but unreachable will reset your connection attempts, while outdated or conflicting cached data can prevent Chrome from establishing a stable link. Other common culprits include unstable Wi-Fi, VPN interference, or antivirus software inspecting your traffic. Understanding these causes helps you target the right fix quickly.

## How to fix ERR_CONNECTION_RESET (Step-by-Step)

1. **Disable the proxy server.** Open Chrome, click the **three-dot menu** in the top-right corner, and go to **Settings**. Select **System**, then click **Open your computer's proxy settings**. Turn off **Use a proxy server** or set it to **Automatically detect settings**. Reload the page to test.

2. **Clear cache and cookies.** In Chrome, press **Ctrl + Shift + Delete** (Windows) or **Cmd + Shift + Delete** (Mac). Choose **All time** as the time range, check **Cookies and other site data** and **Cached images and files**, then click **Clear data**. Restart Chrome afterward.

3. **Reset your network stack.** On Windows, open **Command Prompt** as administrator and run `ipconfig /flushdns`, then `netsh winsock reset`. Reboot your computer to apply the changes.

4. **Check VPN and antivirus.** Temporarily disable any **VPN** or **antivirus firewall** that may be interfering, then retry the site. If it loads, adjust your software's settings to allow Chrome.

## Summary

The **ERR_CONNECTION_RESET** error is usually temporary and fixable with a few targeted adjustments. By disabling problematic proxies, clearing stale cache, and resetting your network, you can restore normal browsing in minutes. If the issue persists, try a different network or contact your ISP for further assistance.