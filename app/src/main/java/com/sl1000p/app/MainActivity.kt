
package com.sl1000p.app

import android.app.Activity
import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient
import android.graphics.Color

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        window.statusBarColor = Color.rgb(10, 14, 22)
        window.navigationBarColor = Color.rgb(10, 14, 22)

        val webView = WebView(this)
        webView.settings.javaScriptEnabled = true
        webView.settings.domStorageEnabled = true
        webView.webViewClient = WebViewClient()

        setContentView(webView)
        webView.loadUrl("https://azisxc830-dot.github.io/Sl1000P/")
    }
}
