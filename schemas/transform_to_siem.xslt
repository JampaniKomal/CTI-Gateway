<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:t="http://ctigateway.example.com/threat"
    exclude-result-prefixes="t">
    
    <xsl:output method="html" indent="yes" encoding="UTF-8" doctype-system="about:legacy-compat"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>SIEM Threat Intelligence Dashboard</title>
                <style>
                    body {
                        background-color: #0d1117;
                        color: #c9d1d9;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        margin: 0;
                        padding: 30px;
                    }
                    h1 {
                        color: #58a6ff;
                        text-align: center;
                        border-bottom: 2px solid #30363d;
                        padding-bottom: 15px;
                        margin-bottom: 30px;
                    }
                    .ioc-card {
                        background-color: #161b22;
                        border: 1px solid #30363d;
                        border-radius: 8px;
                        padding: 20px;
                        margin-bottom: 20px;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
                    }
                    .severity-CRITICAL { color: #f85149; font-weight: bold; }
                    .severity-HIGH { color: #d29922; font-weight: bold; }
                    .severity-MEDIUM { color: #58a6ff; font-weight: bold; }
                    .severity-LOW { color: #3fb950; font-weight: bold; }
                    .ioc-header {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        border-bottom: 1px solid #21262d;
                        padding-bottom: 10px;
                        margin-bottom: 15px;
                    }
                    .ioc-id {
                        font-size: 1.4em;
                        font-weight: bold;
                        color: #ff7b72;
                    }
                    .ioc-type {
                        background-color: #238636;
                        color: #ffffff;
                        padding: 4px 10px;
                        border-radius: 12px;
                        font-size: 0.9em;
                        font-weight: bold;
                    }
                    .ioc-desc {
                        line-height: 1.6;
                        margin-top: 10px;
                        font-size: 1.05em;
                    }
                    .ioc-meta {
                        font-size: 0.9em;
                        color: #8b949e;
                        margin-top: 15px;
                        background-color: #0d1117;
                        padding: 10px;
                        border-radius: 4px;
                    }
                </style>
            </head>
            <body>
                <h1>SIEM Threat Intelligence Dashboard</h1>
                <div class="container">
                    <xsl:for-each select="t:ThreatReport/t:Indicators/t:Indicator">
                        <div class="ioc-card">
                            <div class="ioc-header">
                                <span class="ioc-id"><xsl:value-of select="t:ID"/></span>
                                <span class="ioc-type"><xsl:value-of select="t:Type"/></span>
                            </div>
                            <div>
                                <span>Severity: </span>
                                <span>
                                    <xsl:attribute name="class">severity-<xsl:value-of select="t:Severity"/></xsl:attribute>
                                    <xsl:value-of select="t:Severity"/>
                                </span>
                            </div>
                            <div class="ioc-desc">
                                <xsl:value-of select="t:Description"/>
                            </div>
                            <div class="ioc-meta">
                                <strong>Published:</strong> <xsl:value-of select="t:PublishedDate"/> | 
                                <strong>Source:</strong> <xsl:value-of select="t:Source"/>
                            </div>
                        </div>
                    </xsl:for-each>
                    <xsl:if test="count(t:ThreatReport/t:Indicators/t:Indicator) = 0">
                        <div class="ioc-card" style="text-align: center; color: #8b949e;">
                            No Indicators of Compromise currently tracked.
                        </div>
                    </xsl:if>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
