SELECT date_trunc('month', "Data - FkData"."DataCompleta") AS "Data - FkDataDataCompleta", "Clima Local - FkEstacao"."region" AS "Clima Local - FkEstacaoregion", sum("public"."clima_fatos"."PrecipitacaoTotal") AS "sum"
FROM "public"."clima_fatos"
LEFT JOIN "public"."clima_local" "Clima Local - FkEstacao" ON "public"."clima_fatos"."fkEstacao" = "Clima Local - FkEstacao"."pkEstacao" LEFT JOIN "public"."data" "Data - FkData" ON "public"."clima_fatos"."fkData" = "Data - FkData"."pkData"
WHERE ("Data - FkData"."DataCompleta" >= timestamp with time zone '2021-01-01 00:00:00.000-03:00'
   AND "Data - FkData"."DataCompleta" < timestamp with time zone '2021-05-01 00:00:00.000-03:00')
GROUP BY date_trunc('month', "Data - FkData"."DataCompleta"), "Clima Local - FkEstacao"."region"
ORDER BY date_trunc('month', "Data - FkData"."DataCompleta") ASC, "Clima Local - FkEstacao"."region" ASC
