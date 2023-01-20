SELECT (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')) AS "Data - FkData__DataCompleta", sum("public"."saude_fatos"."Gestante") AS "sum"
FROM "public"."saude_fatos"
LEFT JOIN "public"."data" "Data - FkData" ON "public"."saude_fatos"."fkData" = "Data - FkData"."pkData"
WHERE ("Data - FkData"."Ano" = '2021'
    OR "Data - FkData"."Ano" = '2022')
GROUP BY (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day'))
ORDER BY (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')) ASC